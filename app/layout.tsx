import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ThaiD.online — ศูนย์รวมโซลูชัน AI อัจฉริยะสำหรับคนไทย",
  description:
    "แพลตฟอร์ม SaaS รวมเครื่องมือ AI ครบวงจรสำหรับคนไทย: ระบบสร้างนิยายอัจฉริยะ (Novel Studio), ระบบผลิตและโพสต์คอนเทนต์ Facebook อัตโนมัติ, และระบบออกแบบสติกเกอร์ไลน์ด้วย AI บัญชีเดียวใช้ได้ทุกบริการ",
  keywords: [
    "ThaiD",
    "ThaiD.online",
    "AI แต่งนิยาย",
    "แต่งนิยาย AI",
    "โพสต์ Facebook อัตโนมัติ",
    "สร้างคอนเทนต์ AI",
    "ทำสติกเกอร์ไลน์ AI",
    "LINE Sticker AI",
    "SaaS ไทย",
  ],
  authors: [{ name: "ThaiD Platform Team" }],
  openGraph: {
    title: "ThaiD.online — ยกระดับการสร้างสรรค์ด้วยขุมพลัง AI",
    description:
      "รวมสุดยอดเครื่องมือ AI สำหรับคนไทย ตั้งแต่เขียนนิยาย สร้างคอนเทนต์โซเชียล ไปจนถึงออกแบบสติกเกอร์ไลน์ในแพลตฟอร์มเดียว",
    url: "https://thaid.online",
    siteName: "ThaiD.online",
    locale: "th_TH",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="th" className="scroll-smooth dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Prompt:wght@300;400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-screen bg-[#07090e] text-slate-100 antialiased selection:bg-indigo-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
