import { NextRequest, NextResponse } from "next/server";
import { getCookieDomain, getCorsHeaders } from "@/lib/sso";

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

  const res = NextResponse.json(
    { ok: true, message: "Logged out from ThaiD SSO" },
    { status: 200, headers: getCorsHeaders(origin) }
  );

  // Clear HttpOnly session cookie
  res.cookies.set({
    name: "thaid_session",
    value: "",
    httpOnly: true,
    secure: process.env.NODE_ENV === "production" || !host?.includes("localhost"),
    sameSite: "lax",
    path: "/",
    domain,
    maxAge: 0,
  });

  // Clear client user cookie
  res.cookies.set({
    name: "thaid_user",
    value: "",
    httpOnly: false,
    secure: process.env.NODE_ENV === "production" || !host?.includes("localhost"),
    sameSite: "lax",
    path: "/",
    domain,
    maxAge: 0,
  });

  return res;
}
