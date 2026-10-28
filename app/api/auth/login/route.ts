import { NextRequest, NextResponse } from "next/server";
import { signSSOToken, getCookieDomain, getCorsHeaders, ThaiDUser } from "@/lib/sso";

export async function OPTIONS(req: NextRequest) {
  const origin = req.headers.get("origin");
  return new NextResponse(null, {
    status: 204,
    headers: getCorsHeaders(origin),
  });
}

export async function POST(req: NextRequest) {
  const origin = req.headers.get("origin");
  const host = req.headers.get("host");
  const domain = getCookieDomain(host);

  try {
    const body = await req.json();
    const email = (body.email || "").trim().toLowerCase();
    
    if (!email) {
      return NextResponse.json(
        { ok: false, error: "Email is required" },
        { status: 400, headers: getCorsHeaders(origin) }
      );
    }

    const isSuperAdmin = email === "iamjotaki@gmail.com";
    const isAdmin = isSuperAdmin || email === "admin@thaid.online" || email.includes("admin");

    const ALL_SERVICES = ["novel", "social", "vault", "sticker", "clip", "chat", "mockup"];

    let name = body.name || email.split("@")[0];
    let avatar = body.avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(name)}`;
    let role = isSuperAdmin ? "superadmin" : (isAdmin ? "admin" : "member");
    let plan = isSuperAdmin ? "Owner & Super Admin (All Access)" : (isAdmin ? "VIP Enterprise" : "Free Member");
    let credits = isSuperAdmin ? 999999 : (isAdmin ? 9999 : 0);
    let subscriptions = isSuperAdmin || isAdmin ? ALL_SERVICES : (body.subscriptions || []);

    if (isSuperAdmin) {
      name = "Jotaki";
    }

    const user: ThaiDUser = {
      id: isSuperAdmin ? "u_jotaki_root" : "u_" + Math.random().toString(36).substring(2, 10),
      name,
      email,
      avatar,
      role,
      plan,
      credits,
      subscriptions,
      createdAt: Date.now(),
    };

    const token = signSSOToken(user);

    const res = NextResponse.json(
      { ok: true, user, token },
      { status: 200, headers: getCorsHeaders(origin) }
    );

    // 1. Secure HttpOnly session cookie for all *.thaid.online
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

    // 2. Client-readable user info cookie for instant UI hydration across all *.thaid.online
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
      { ok: false, error: err.message || "Failed to process login" },
      { status: 500, headers: getCorsHeaders(origin) }
    );
  }
}
