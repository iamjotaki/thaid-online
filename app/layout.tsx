import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ThaiD.online — Show the world what AI can do",
  description:
    "ศูนย์รวมเครื่องมือ AI อัจฉริยะมาตรฐานระดับโลก ออกแบบมาเพื่อคนไทยโดยเฉพาะ: ReadAWrite Pro Studio แต่งนิยายอัตโนมัติ, ระบบสร้างคอนเทนต์ & วิดีโอโพสต์ Facebook, และระบบเจนสติกเกอร์ไลน์",
  keywords: [
    "ThaiD",
    "ThaiD.online",
    "Fastwork AI",
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
    title: "ThaiD.online — Show the world what AI can do",
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
  themeColor: "#ffffff",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="th" className="scroll-smooth bg-white text-[#171717]">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        {/* Google Sans, Noto Sans Thai, Charm (Calligraphy), Plus Jakarta Sans */}
        <link
          href="https://fonts.googleapis.com/css2?family=Charm:wght@400;700&family=Google+Sans:wght@400;500;700&family=Noto+Sans+Thai:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap"
          rel="stylesheet"
        />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
        />
      </head>
      <body className="min-h-screen bg-white text-[#171717] antialiased selection:bg-[#0569ff]/15 selection:text-[#0569ff]">
        {children}
      </body>
    </html>
  );
}
