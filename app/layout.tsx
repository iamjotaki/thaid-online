import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ThaiD.online — Luxury AI Ecosystem สำหรับคนไทย",
  description:
    "ศูนย์รวมเครื่องมือ AI อัจฉริยะมาตรฐานระดับโลก ออกแบบมาเพื่อคนไทยโดยเฉพาะ: ReadAWrite Pro Studio แต่งนิยายอัตโนมัติ, ระบบสร้างคอนเทนต์ & วิดีโอโพสต์ Facebook, และระบบเจนสติกเกอร์ไลน์",
  keywords: [
    "ThaiD",
    "ThaiD.online",
    "ReadAWrite AI",
    "แต่งนิยาย AI",
    "Auto Post Facebook",
    "AI โพสต์เฟสบุ๊ค",
    "LINE Sticker AI",
    "สร้างสติกเกอร์ไลน์",
    "SaaS ไทย",
  ],
  authors: [{ name: "ThaiD Platform Team" }],
  openGraph: {
    title: "ThaiD.online — Luxury AI Ecosystem สำหรับคนไทย",
    description:
      "ศูนย์รวมเครื่องมือ AI อัจฉริยะมาตรฐานระดับโลก แต่งนิยาย สร้างคอนเทนต์โซเชียล สติกเกอร์ไลน์ ในแพลตฟอร์มเดียว",
    url: "https://thaid.online",
    siteName: "ThaiD.online",
    locale: "th_TH",
    type: "website",
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  themeColor: "#131922",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="th" className="scroll-smooth dark bg-[#131922] text-[#fafafa]">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Google+Sans:ital,opsz,wght@0,17..18,400..700;1,17..18,400..700&family=Noto+Sans+Thai:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
          rel="stylesheet"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="antialiased selection:bg-[#0074e2]/30 selection:text-white custom-scrollbar bg-[#141414] text-[#f5f5f7]">
        {children}
      </body>
    </html>
  );
}
