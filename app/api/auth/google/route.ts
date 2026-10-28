import { NextRequest, NextResponse } from "next/server";
import { signSSOToken, getCookieDomain, getCorsHeaders, ThaiDUser } from "@/lib/sso";

export async function OPTIONS(req: NextRequest) {
  const origin = req.headers.get("origin");
  return new NextResponse(null, {
    status: 204,
    headers: getCorsHeaders(origin),
  });
}

/**
 * GET /api/auth/google
 * Initiates the Google OAuth 2.0 authorization redirect.
 */
export async function GET(req: NextRequest) {
  const host = req.headers.get("host") || "thaid.online";
  const searchParams = req.nextUrl.searchParams;
  const returnTo = searchParams.get("from") || `https://${host}`;

  const clientId = process.env.GOOGLE_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_CLIENT_SECRET;

  if (!clientId || !clientSecret) {
    // If Google credentials are not yet configured in environment variables,
    // return an informative response with setup instructions or fallback
    const origin = req.headers.get("origin");
    return NextResponse.json(
      {
        ok: false,
        error: "Google OAuth is not configured yet.",
        message: "Please configure GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET in environment variables.",
        setupGuide: {
          callbackUrl: `https://${host}/api/auth/google/callback`,
          origins: [
            `https://${host}`,
            "https://thaid.online",
            "https://novel.thaid.online",
            "https://social.thaid.online",
            "https://vault.thaid.online",
            "https://sticker.thaid.online",
            "https://clip.thaid.online",
            "https://chat.thaid.online",
            "https://mockup.thaid.online",
          ],
        },
      },
      { status: 503, headers: getCorsHeaders(origin) }
    );
  }

  const redirectUri = `https://${host}/api/auth/google/callback`;
  const state = Buffer.from(JSON.stringify({ returnTo, timestamp: Date.now() })).toString("base64");

  const googleAuthUrl = new URL("https://accounts.google.com/o/oauth2/v2/auth");
  googleAuthUrl.searchParams.set("client_id", clientId);
  googleAuthUrl.searchParams.set("redirect_uri", redirectUri);
  googleAuthUrl.searchParams.set("response_type", "code");
  googleAuthUrl.searchParams.set("scope", "openid email profile");
  googleAuthUrl.searchParams.set("state", state);
  googleAuthUrl.searchParams.set("access_type", "online");
  googleAuthUrl.searchParams.set("prompt", "select_account");

  return NextResponse.redirect(googleAuthUrl.toString());
}

/**
 * POST /api/auth/google
 * Verifies Google ID Token (from Google Identity Services / One Tap) and issues SSO wildcard cookies.
 */
export async function POST(req: NextRequest) {
  const origin = req.headers.get("origin");
  const host = req.headers.get("host") || "thaid.online";
  const domain = getCookieDomain(host);

  try {
    const body = await req.json();
    const idToken = (body.id_token || body.credential || "").trim();

    if (!idToken) {
      return NextResponse.json(
        { ok: false, error: "ID token is required" },
        { status: 400, headers: getCorsHeaders(origin) }
      );
    }

    // Verify token with Google TokenInfo API
    const verifyRes = await fetch(`https://oauth2.googleapis.com/tokeninfo?id_token=${encodeURIComponent(idToken)}`);
    if (!verifyRes.ok) {
      const errData = await verifyRes.json();
      return NextResponse.json(
        { ok: false, error: "Invalid Google ID token", details: errData },
        { status: 401, headers: getCorsHeaders(origin) }
      );
    }

    const payload = await verifyRes.json();
    const email = (payload.email || "").trim().toLowerCase();
    const name = payload.name || email.split("@")[0] || "Google User";
    const avatar = payload.picture || `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(name)}`;
    const googleSub = payload.sub || "g_" + Math.random().toString(36).substring(2, 10);

    if (!email) {
      return NextResponse.json(
        { ok: false, error: "Google account did not return an email address" },
        { status: 400, headers: getCorsHeaders(origin) }
      );
    }

    // Determine user role and plan
    const isAdmin =
      email === "boss@thaid.online" ||
      email === "admin@thaid.online" ||
      email === "iamjotaki@gmail.com" ||
      email.includes("admin");

    const user: ThaiDUser = {
      id: "g_" + googleSub,
      name,
      email,
      avatar,
      role: isAdmin ? "admin" : "member",
      plan: isAdmin ? "VIP Enterprise" : "Free Trial",
      credits: isAdmin ? 9999 : 50,
      createdAt: Date.now(),
    };

    const token = signSSOToken(user);

    const res = NextResponse.json(
      { ok: true, user, token, message: "Logged in via Google Account successfully" },
      { status: 200, headers: getCorsHeaders(origin) }
    );

    // Set SSO wildcard cookies
    res.cookies.set({
      name: "thaid_session",
      value: token,
      httpOnly: true,
      secure: process.env.NODE_ENV === "production" || !host?.includes("localhost"),
      sameSite: "lax",
      path: "/",
      domain,
      maxAge: 60 * 60 * 24 * 30, // 30 days
    });

    res.cookies.set({
      name: "thaid_user",
      value: JSON.stringify(user),
      httpOnly: false,
      secure: process.env.NODE_ENV === "production" || !host?.includes("localhost"),
      sameSite: "lax",
      path: "/",
      domain,
      maxAge: 60 * 60 * 24 * 30, // 30 days
    });

    return res;
  } catch (err: any) {
    return NextResponse.json(
      { ok: false, error: err.message || "Failed to process Google authentication" },
      { status: 500, headers: getCorsHeaders(origin) }
    );
  }
}
