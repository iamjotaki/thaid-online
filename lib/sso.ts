import crypto from "node:crypto";

export interface ThaiDUser {
  id?: string;
  name: string;
  email: string;
  avatar?: string;
  role?: string;
  plan?: string;
  credits?: number;
  createdAt?: number;
}

const DEFAULT_SECRET = process.env.JWT_SECRET || "thaid-super-sso-secret-prod-2026-secure";

export function base64url(str: string): string {
  return Buffer.from(str)
    .toString("base64")
    .replace(/=/g, "")
    .replace(/\+/g, "-")
    .replace(/\//g, "_");
}

export function base64urlDecode(str: string): string {
  let base64 = str.replace(/-/g, "+").replace(/_/g, "/");
  while (base64.length % 4) {
    base64 += "=";
  }
  return Buffer.from(base64, "base64").toString("utf-8");
}

export function signSSOToken(user: ThaiDUser, secret = DEFAULT_SECRET): string {
  const header = base64url(JSON.stringify({ alg: "HS256", typ: "JWT" }));
  const exp = Math.floor(Date.now() / 1000) + 60 * 60 * 24 * 30; // 30 days
  const payload = base64url(JSON.stringify({ ...user, exp }));
  const data = `${header}.${payload}`;
  const signature = crypto
    .createHmac("sha256", secret)
    .update(data)
    .digest("base64")
    .replace(/=/g, "")
    .replace(/\+/g, "-")
    .replace(/\//g, "_");
  return `${data}.${signature}`;
}

export function verifySSOToken(token: string, secret = DEFAULT_SECRET): ThaiDUser | null {
  try {
    const parts = token.split(".");
    if (parts.length !== 3) return null;
    const [header, payload, signature] = parts;
    const expectedSig = crypto
      .createHmac("sha256", secret)
      .update(`${header}.${payload}`)
      .digest("base64")
      .replace(/=/g, "")
      .replace(/\+/g, "-")
      .replace(/\//g, "_");
    if (signature !== expectedSig) return null;
    const decoded = JSON.parse(base64urlDecode(payload));
    if (decoded.exp && decoded.exp < Math.floor(Date.now() / 1000)) {
      return null;
    }
    return decoded as ThaiDUser;
  } catch {
    return null;
  }
}

export function getCookieDomain(host?: string | null): string | undefined {
  if (!host) return ".thaid.online";
  const clean = host.split(":")[0];
  if (clean.includes("localhost") || clean.includes("127.0.0.1") || /^\d+\.\d+\.\d+\.\d+$/.test(clean)) {
    return undefined;
  }
  return ".thaid.online";
}

export function getCorsHeaders(origin: string | null) {
  let allowedOrigin = "https://thaid.online";
  if (origin) {
    const isThaiD = origin === "https://thaid.online" || origin.endsWith(".thaid.online");
    const isLocal = origin.includes("localhost") || origin.includes("127.0.0.1");
    if (isThaiD || isLocal) {
      allowedOrigin = origin;
    }
  }

  return {
    "Access-Control-Allow-Origin": allowedOrigin,
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
  };
}
