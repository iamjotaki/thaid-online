import { NextRequest, NextResponse } from "next/server";
import { signSSOToken, getCookieDomain, ThaiDUser } from "@/lib/sso";

/**
 * GET /api/auth/google/callback
 * Handles the redirect from Google OAuth consent screen with authorization code.
 */
export async function GET(req: NextRequest) {
  const host = req.headers.get("host") || "thaid.online";
  const domain = getCookieDomain(host);
  const searchParams = req.nextUrl.searchParams;

  const code = searchParams.get("code");
  const stateParam = searchParams.get("state");
  const error = searchParams.get("error");

  let returnTo = `https://${host}`;
  if (stateParam) {
    try {
      const decodedState = JSON.parse(Buffer.from(stateParam, "base64").toString("utf-8"));
      if (decodedState.returnTo) {
        returnTo = decodedState.returnTo;
      }
    } catch (e) {}
  }

  if (error || !code) {
    const errorUrl = new URL(returnTo);
    errorUrl.searchParams.set("auth_error", error || "access_denied");
    return NextResponse.redirect(errorUrl.toString());
  }

  const clientId = process.env.GOOGLE_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_CLIENT_SECRET;

  if (!clientId || !clientSecret) {
    const errorUrl = new URL(returnTo);
    errorUrl.searchParams.set("auth_error", "missing_google_credentials");
    return NextResponse.redirect(errorUrl.toString());
  }

  try {
    const redirectUri = `https://${host}/api/auth/google/callback`;

    // 1. Exchange authorization code for tokens
    const tokenRes = await fetch("https://oauth2.googleapis.com/token", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        code,
        client_id: clientId,
        client_secret: clientSecret,
        redirect_uri: redirectUri,
        grant_type: "authorization_code",
      }).toString(),
    });

    if (!tokenRes.ok) {
      const errDetails = await tokenRes.text();
      console.error("Google token exchange error:", errDetails);
      const errUrl = new URL(returnTo);
      errUrl.searchParams.set("auth_error", "token_exchange_failed");
      return NextResponse.redirect(errUrl.toString());
    }

    const tokenData = await tokenRes.json();
    const accessToken = tokenData.access_token;

    // 2. Fetch user profile from OpenID Connect userinfo endpoint
    const userinfoRes = await fetch("https://openidconnect.googleapis.com/v1/userinfo", {
      headers: { Authorization: `Bearer ${accessToken}` },
    });

    if (!userinfoRes.ok) {
      const errUrl = new URL(returnTo);
      errUrl.searchParams.set("auth_error", "userinfo_fetch_failed");
      return NextResponse.redirect(errUrl.toString());
    }

    const profile = await userinfoRes.json();
    const email = (profile.email || "").trim().toLowerCase();
    const name = profile.name || email.split("@")[0] || "Google User";
    const avatar = profile.picture || `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(name)}`;
    const googleSub = profile.sub || "g_" + Math.random().toString(36).substring(2, 10);

    const isSuperAdmin = email === "iamjotaki@gmail.com";
    const isAdmin = isSuperAdmin || email === "boss@thaid.online" || email === "admin@thaid.online" || email.includes("admin");

    const ALL_SERVICES = ["novel", "social", "vault", "sticker", "clip", "chat", "mockup"];

    const user: ThaiDUser = {
      id: isSuperAdmin ? "u_jotaki_root" : "g_" + googleSub,
      name: isSuperAdmin ? "Jotaki" : name,
      email,
      avatar: avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(name)}`,
      role: isSuperAdmin ? "superadmin" : (isAdmin ? "admin" : "member"),
      plan: isSuperAdmin ? "Owner & Super Admin (All Access)" : (isAdmin ? "VIP Enterprise" : "Free Member"),
      credits: isSuperAdmin ? 999999 : (isAdmin ? 9999 : 0),
      subscriptions: isSuperAdmin || isAdmin ? ALL_SERVICES : [],
      createdAt: Date.now(),
    };

    const token = signSSOToken(user);

    // 3. Set wildcard SSO cookies on redirect response
    const successRedirectUrl = new URL(returnTo);
    successRedirectUrl.searchParams.set("auth_success", "google");

    const redirectResponse = NextResponse.redirect(successRedirectUrl.toString());

    redirectResponse.cookies.set({
      name: "thaid_session",
      value: token,
      httpOnly: true,
      secure: process.env.NODE_ENV === "production" || !host?.includes("localhost"),
      sameSite: "lax",
      path: "/",
      domain,
      maxAge: 60 * 60 * 24 * 30, // 30 days
    });

    redirectResponse.cookies.set({
      name: "thaid_user",
      value: JSON.stringify(user),
      httpOnly: false,
      secure: process.env.NODE_ENV === "production" || !host?.includes("localhost"),
      sameSite: "lax",
      path: "/",
      domain,
      maxAge: 60 * 60 * 24 * 30, // 30 days
    });

    return redirectResponse;
  } catch (err: any) {
    console.error("Google OAuth callback exception:", err);
    const errUrl = new URL(returnTo);
    errUrl.searchParams.set("auth_error", "oauth_exception");
    return NextResponse.redirect(errUrl.toString());
  }
}
