import { type NextRequest, NextResponse } from "next/server"
import { AuditEngine } from "@/lib/audit-engine"

export async function POST(request: NextRequest) {
  try {
    let body
    try {
      body = await request.json()
    } catch (jsonError) {
      console.error("JSON parsing error:", jsonError)
      return NextResponse.json({ error: "Invalid JSON in request body" }, { status: 400 })
    }

    if (!body || typeof body !== "object" || !body.url) {
      return NextResponse.json({ error: "URL is required in request body" }, { status: 400 })
    }

    const { url } = body

    if (typeof url !== "string" || url.trim().length === 0) {
      return NextResponse.json({ error: "URL must be a non-empty string" }, { status: 400 })
    }

    // Validate URL format
    try {
      const testUrl = url.startsWith("http") ? url : `https://${url}`
      new URL(testUrl)
    } catch (urlError) {
      return NextResponse.json({ error: "Invalid URL format" }, { status: 400 })
    }

    console.log(`🔍 API: Starting analysis for ${url}`)

    const engine = new AuditEngine()
    const result = await engine.auditWebsite(url.trim())

    // Ensure all numeric values are properly converted
    const sanitizedResult = {
      ...result,
      overallScore: Number(result.overallScore) || 0,
      crawlability_score: Number(result.crawlability_score) || 0,
      confidence: Number(result.confidence) || 0,
      analysis_time: Number(result.analysis_time) || 0,
      modules: result.modules.map((module) => ({
        ...module,
        score: Number(module.score) || 0,
      })),
      features: Object.fromEntries(
        Object.entries(result.features || {}).map(([key, value]) => [
          key,
          typeof value === "string"
            ? value
            : typeof value === "boolean"
              ? value
              : typeof value === "number"
                ? value
                : value != null
                  ? String(value)
                  : null,
        ]),
      ),
    }

    console.log(
      `✅ API: Analysis completed for ${url} - Score: ${sanitizedResult.overallScore}%, Valid: ${sanitizedResult.validationResult?.isValid}`,
    )

    return NextResponse.json(sanitizedResult, {
      headers: {
        "Content-Type": "application/json",
      },
    })
  } catch (error) {
    console.error("❌ API: Analysis failed:", error)

    const errorMessage = error instanceof Error ? error.message : "Unknown error occurred"
    const errorResponse = {
      error: "Analysis failed",
      message: errorMessage,
      timestamp: new Date().toISOString(),
    }

    return NextResponse.json(errorResponse, { status: 500 })
  }
}

export async function GET() {
  return NextResponse.json({
    message: "Production Website Audit Tool API",
    version: "2.0.0",
    features: [
      "Google Search Verification",
      "Real-time Website Analysis",
      "Fake URL Protection",
      "Comprehensive SEO Audit",
      "Performance Analysis",
      "Security Assessment",
      "Mobile Optimization Check",
    ],
    endpoints: {
      analyze: "POST /api/analyze",
    },
  })
}
