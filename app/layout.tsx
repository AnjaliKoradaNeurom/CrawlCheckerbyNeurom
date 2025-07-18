<<<<<<< HEAD
import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'v0 App',
  description: 'Created with v0',
  generator: 'v0.dev',
=======
import type React from "react"
import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "Production Website Audit Tool - Advanced SEO & Performance Analysis",
  description:
    "Professional website audit tool with AI-powered crawlability analysis, SEO optimization, performance testing, and security scanning. Get detailed recommendations to improve your website's search engine ranking.",
  keywords: "website audit, SEO analysis, performance testing, crawlability, security scan, web vitals, technical SEO",
  authors: [{ name: "Web Audit Tool" }],
  creator: "Web Audit Tool",
  publisher: "Web Audit Tool",
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://your-domain.com",
    title: "Production Website Audit Tool - Advanced SEO & Performance Analysis",
    description: "Professional website audit tool with AI-powered analysis and detailed optimization recommendations.",
    siteName: "Web Audit Tool",
    images: [
      {
        url: "/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Website Audit Tool Dashboard",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Production Website Audit Tool",
    description: "Professional website audit with AI-powered analysis",
    images: ["/twitter-image.jpg"],
  },
  verification: {
    google: "your-google-verification-code",
    yandex: "your-yandex-verification-code",
  },
  alternates: {
    canonical: "https://your-domain.com",
  },
    generator: 'v0.dev'
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
<<<<<<< HEAD
  return (
    <html lang="en">
=======
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    name: "Production Website Audit Tool",
    description:
      "Professional website audit tool with AI-powered crawlability analysis, SEO optimization, and performance testing.",
    url: "https://your-domain.com",
    applicationCategory: "BusinessApplication",
    operatingSystem: "Web Browser",
    offers: {
      "@type": "Offer",
      price: "0",
      priceCurrency: "USD",
    },
    creator: {
      "@type": "Organization",
      name: "Web Audit Tool",
      url: "https://your-domain.com",
    },
    featureList: [
      "SEO Analysis",
      "Performance Testing",
      "Security Scanning",
      "Crawlability Assessment",
      "Web Vitals Monitoring",
    ],
  }

  return (
    <html lang="en">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(structuredData),
          }}
        />
      </head>
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
      <body>{children}</body>
    </html>
  )
}
