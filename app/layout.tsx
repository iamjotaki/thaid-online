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
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#f5f5f7" },
    { media: "(prefers-color-scheme: dark)", color: "#0c0c0e" },
  ],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="th" className="scroll-smooth dark" suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var s=localStorage.getItem('thaid-theme');if(s==='light'){document.documentElement.classList.remove('dark');document.documentElement.classList.add('light');}else{document.documentElement.classList.add('dark');document.documentElement.classList.remove('light');}}catch(e){}})();`,
          }}
        />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap"
          rel="stylesheet"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="antialiased selection:bg-orange-500/20 selection:text-[#e85a2d] custom-scrollbar">
        {children}
      </body>
    </html>
  );
}
