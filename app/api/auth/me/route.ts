import { NextRequest, NextResponse } from "next/server";
import { verifySSOToken, getCorsHeaders } from "@/lib/sso";

export async function OPTIONS(req: NextRequest) {
  const origin = req.headers.get("origin");
  return new NextResponse(null, {
    status: 204,
    headers: getCorsHeaders(origin),
  });
}

export async function GET(req: NextRequest) {
  const origin = req.headers.get("origin");

  // Read session token from HttpOnly cookie or Authorization header
  let token = req.cookies.get("thaid_session")?.value;
  if (!token) {
    const authHeader = req.headers.get("authorization");
    if (authHeader && authHeader.startsWith("Bearer ")) {
      token = authHeader.substring(7).trim();
    }
  }

  if (!token) {
    return NextResponse.json(
      { ok: true, authenticated: false, user: null },
      { status: 200, headers: getCorsHeaders(origin) }
    );
  }

  const user = verifySSOToken(token);
  if (!user) {
    return NextResponse.json(
      { ok: true, authenticated: false, user: null },
      { status: 200, headers: getCorsHeaders(origin) }
    );
  }

  return NextResponse.json(
    { ok: true, authenticated: true, user },
    { status: 200, headers: getCorsHeaders(origin) }
  );
}
