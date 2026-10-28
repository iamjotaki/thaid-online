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

    // Standard preset or custom user mapping
    let name = body.name || email.split("@")[0];
    let avatar = body.avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(name)}`;
    let role = body.role || (email.includes("admin") || email === "iamjotaki@gmail.com" ? "admin" : "member");
    let plan = body.plan || (role === "admin" ? "VIP Enterprise" : "Free Trial");

    if (email === "admin@thaid.online" || email === "admin@lfcautonews.com" || email === "boss@fanpage.com") {
      name = "Admin Boss";
      role = "admin";
      plan = "VIP Enterprise";
      avatar = "https://api.dicebear.com/7.x/bottts/svg?seed=AdminBoss";
    }

    const user: ThaiDUser = {
      id: "u_" + Math.random().toString(36).substring(2, 10),
      name,
      email,
      avatar,
      role,
      plan,
      credits: role === "admin" ? 9999 : 50,
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
