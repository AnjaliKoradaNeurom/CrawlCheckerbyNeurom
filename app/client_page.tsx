"use client"

<<<<<<< HEAD
import { useState, useEffect } from "react"
=======
import { useState, Suspense } from "react"
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Progress } from "@/components/ui/progress"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { Separator } from "@/components/ui/separator"
<<<<<<< HEAD
import { CircularScore } from "@/components/ui/circular-score"
=======
import { CircularScore } from "@/components/circular-score"
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
import ExportManager from "@/components/export-manager"
import {
  Search,
  Globe,
  Shield,
  Smartphone,
  Zap,
  Download,
  AlertTriangle,
  CheckCircle,
  Clock,
  ExternalLink,
<<<<<<< HEAD
  RefreshCw,
  Wifi,
  WifiOff,
} from "lucide-react"

// Updated types to match backend response
interface Recommendation {
  priority: string
  title: string
  message: string
  code_snippet?: string
  doc_link?: string
}

interface ModuleResult {
  name: string
  score: number
  description: string
  explanation: string
  recommendations: Recommendation[]
}

interface AnalysisResult {
  url: string
  timestamp: string
  overall_score: number
  modules: ModuleResult[]
  analysis_time: number
}

interface BackendStatus {
  status: string
  backend?: any
  error?: string
}
=======
  ShieldCheck,
  XCircle,
} from "lucide-react"
import type { AuditResult } from "@/lib/types"
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b

export default function WebAuditToolClient() {
  const [url, setUrl] = useState("")
  const [isAnalyzing, setIsAnalyzing] = useState(false)
<<<<<<< HEAD
  const [result, setResult] = useState<AnalysisResult | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [backendStatus, setBackendStatus] = useState<BackendStatus | null>(null)
  const [isCheckingBackend, setIsCheckingBackend] = useState(false)

  // Check backend status on component mount
  useEffect(() => {
    checkBackendStatus()
  }, [])

  const checkBackendStatus = async () => {
    setIsCheckingBackend(true)
    try {
      const response = await fetch("/api/analyze", {
        method: "GET",
      })
      const data = await response.json()
      setBackendStatus(data)
    } catch (err) {
      setBackendStatus({
        status: "Backend connection failed",
        error: err instanceof Error ? err.message : "Unknown error",
      })
    } finally {
      setIsCheckingBackend(false)
    }
  }
=======
  const [result, setResult] = useState<AuditResult | null>(null)
  const [error, setError] = useState<string | null>(null)
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b

  const handleAnalyze = async () => {
    if (!url.trim()) {
      setError("Please enter a valid URL")
      return
    }

<<<<<<< HEAD
    // Check if backend is available before starting analysis
    if (backendStatus?.status !== "Backend connected") {
      setError("Backend service is not available. Please start the Python API server.")
      return
    }

=======
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    setIsAnalyzing(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: url.trim() }),
      })

<<<<<<< HEAD
      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || `HTTP ${response.status}`)
      }

      // Transform backend response to match frontend expectations
      const transformedResult: AnalysisResult = {
        url: data.url,
        timestamp: data.timestamp,
        overall_score: data.overall_score,
        modules: data.modules.map((module: any) => ({
          name: module.name,
          score: module.score,
          description: module.description,
          explanation: module.explanation,
          recommendations: module.recommendations.map((rec: any) => ({
            priority: rec.priority,
            title: rec.title,
            message: rec.message,
            codeSnippet: rec.code_snippet,
            docLink: rec.doc_link,
          })),
        })),
        analysis_time: data.analysis_time,
      }

      setResult(transformedResult)
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : "Analysis failed"
      setError(errorMessage)

      // If it's a backend connectivity issue, refresh backend status
      if (errorMessage.includes("Backend") || errorMessage.includes("unavailable")) {
        checkBackendStatus()
      }
=======
      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || `HTTP ${response.status}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Analysis failed")
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    } finally {
      setIsAnalyzing(false)
    }
  }

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case "High":
        return "destructive"
      case "Medium":
        return "default"
      case "Low":
        return "secondary"
      default:
        return "default"
    }
  }

  const getScoreColor = (score: number) => {
    if (score >= 80) return "text-green-600"
    if (score >= 60) return "text-yellow-600"
    return "text-red-600"
  }

  const getScoreLabel = (score: number) => {
    if (score >= 90) return "Excellent"
    if (score >= 80) return "Good"
    if (score >= 60) return "Fair"
    if (score >= 40) return "Poor"
    return "Critical"
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center mb-4">
            <Globe className="h-12 w-12 text-blue-600 mr-3" />
<<<<<<< HEAD
            <h1 className="text-4xl font-bold text-gray-900">Website Audit Tool</h1>
          </div>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Advanced website analysis powered by Python backend API
          </p>
          <div className="flex items-center justify-center mt-4 space-x-4">
            <Badge variant="outline" className="text-blue-600">
              <Zap className="h-3 w-3 mr-1" />
              API-Powered
            </Badge>
            <Badge variant="outline" className="text-purple-600">
              <Shield className="h-3 w-3 mr-1" />
              Backend Analysis
=======
            <h1 className="text-4xl font-bold text-gray-900">Production Website Audit Tool</h1>
          </div>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Advanced real-time website analysis with Google verification for legitimate websites only
          </p>
          <div className="flex items-center justify-center mt-4 space-x-4">
            <Badge variant="outline" className="text-green-600">
              <ShieldCheck className="h-3 w-3 mr-1" />
              Google Verified
            </Badge>
            <Badge variant="outline" className="text-blue-600">
              <Zap className="h-3 w-3 mr-1" />
              Real-time Analysis
            </Badge>
            <Badge variant="outline" className="text-purple-600">
              <Shield className="h-3 w-3 mr-1" />
              Fake URL Protection
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
            </Badge>
          </div>
        </div>

<<<<<<< HEAD
        {/* Backend Status */}
        <Card className="max-w-2xl mx-auto mb-4">
          <CardContent className="pt-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                {backendStatus?.status === "Backend connected" ? (
                  <Wifi className="h-4 w-4 text-green-600" />
                ) : (
                  <WifiOff className="h-4 w-4 text-red-600" />
                )}
                <span className="text-sm font-medium">Backend Status: {backendStatus?.status || "Checking..."}</span>
              </div>
              <Button variant="outline" size="sm" onClick={checkBackendStatus} disabled={isCheckingBackend}>
                {isCheckingBackend ? <RefreshCw className="h-3 w-3 animate-spin" /> : <RefreshCw className="h-3 w-3" />}
              </Button>
            </div>
            {backendStatus?.error && <p className="text-xs text-red-600 mt-2">{backendStatus.error}</p>}
          </CardContent>
        </Card>

=======
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        {/* Analysis Form */}
        <Card className="max-w-2xl mx-auto mb-8">
          <CardHeader>
            <CardTitle className="flex items-center">
              <Search className="h-5 w-5 mr-2" />
<<<<<<< HEAD
              Analyze Website
            </CardTitle>
            <CardDescription>Enter a website URL - analysis will be performed by our Python backend</CardDescription>
=======
              Analyze Legitimate Website
            </CardTitle>
            <CardDescription>
              Enter a website URL - we'll verify it's legitimate through Google before analysis
            </CardDescription>
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
          </CardHeader>
          <CardContent>
            <div className="flex gap-4">
              <Input
                type="url"
                placeholder="https://example.com"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                onKeyPress={(e) => e.key === "Enter" && handleAnalyze()}
                className="flex-1"
<<<<<<< HEAD
                disabled={backendStatus?.status !== "Backend connected"}
              />
              <Button
                onClick={handleAnalyze}
                disabled={isAnalyzing || backendStatus?.status !== "Backend connected"}
                className="px-8"
              >
                {isAnalyzing ? (
                  <>
                    <Clock className="h-4 w-4 mr-2 animate-spin" />
                    Analyzing...
=======
              />
              <Button onClick={handleAnalyze} disabled={isAnalyzing} className="px-8">
                {isAnalyzing ? (
                  <>
                    <Clock className="h-4 w-4 mr-2 animate-spin" />
                    Validating & Analyzing...
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
                  </>
                ) : (
                  "Analyze"
                )}
              </Button>
            </div>
<<<<<<< HEAD

=======
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
            {error && (
              <Alert className="mt-4" variant="destructive">
                <AlertTriangle className="h-4 w-4" />
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}
<<<<<<< HEAD

            {backendStatus?.status !== "Backend connected" && (
              <Alert className="mt-4" variant="destructive">
                <WifiOff className="h-4 w-4" />
                <AlertDescription>
                  Backend API is not available. Please start the Python server using:
                  <code className="block mt-2 p-2 bg-gray-100 rounded text-sm">
                    cd backend && python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
                  </code>
                </AlertDescription>
              </Alert>
            )}

            <div className="mt-4 text-sm text-gray-600">
              <p className="font-medium mb-2">Analysis powered by:</p>
              <ul className="space-y-1 text-xs">
                <li>• Python FastAPI backend for comprehensive analysis</li>
                <li>• Real-time SEO and performance evaluation</li>
                <li>• Security and mobile-friendliness assessment</li>
                <li>• No client-side processing - all data from API</li>
=======
            <div className="mt-4 text-sm text-gray-600">
              <p className="font-medium mb-2">Our validation process:</p>
              <ul className="space-y-1 text-xs">
                <li>• URL format and accessibility check</li>
                <li>• Google Search verification for legitimacy</li>
                <li>• Content quality and structure validation</li>
                <li>• Fake/suspicious URL pattern detection</li>
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
              </ul>
            </div>
          </CardContent>
        </Card>

<<<<<<< HEAD
        {/* Results - Only show if we have valid backend data */}
        {result && (
          <div className="space-y-8">
            {/* Overview */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center justify-between">
                  <span>Website Analysis Results</span>
                  <Badge variant="outline" className="text-green-600">
                    <CheckCircle className="h-3 w-3 mr-1" />
                    Backend Analyzed
                  </Badge>
                </CardTitle>
                <CardDescription>
                  Analyzed: {result.url} • {new Date(result.timestamp).toLocaleString()}
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                  {/* Overall Score */}
                  <div className="text-center">
                    <CircularScore score={result.overall_score} size={120} />
                    <h3 className="font-semibold mt-2">Overall Score</h3>
                    <p className={`text-sm ${getScoreColor(result.overall_score)}`}>
                      {getScoreLabel(result.overall_score)}
                    </p>
                  </div>

                  {/* Module Scores */}
                  {result.modules.slice(0, 3).map((module) => (
                    <div key={module.name} className="text-center">
                      <CircularScore score={module.score} size={80} />
                      <h4 className="font-medium mt-2 text-sm">{module.name}</h4>
                      <p className={`text-xs ${getScoreColor(module.score)}`}>{getScoreLabel(module.score)}</p>
                    </div>
                  ))}
                </div>

                <Separator className="my-6" />

                {/* Key Metrics */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                  <div>
                    <p className="text-gray-600">Overall Score</p>
                    <p className="font-semibold">{result.overall_score}%</p>
                  </div>
                  <div>
                    <p className="text-gray-600">Data Source</p>
                    <p className="font-semibold text-green-600">Backend API</p>
                  </div>
                  <div>
                    <p className="text-gray-600">Analysis Time</p>
                    <p className="font-semibold">{result.analysis_time.toFixed(2)}s</p>
                  </div>
                  <div>
                    <p className="text-gray-600">Modules</p>
                    <p className="font-semibold">{result.modules.length}</p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Detailed Results */}
            <Tabs defaultValue="recommendations" className="w-full">
              <TabsList className="grid w-full grid-cols-3">
                <TabsTrigger value="recommendations">Recommendations</TabsTrigger>
                <TabsTrigger value="modules">Module Details</TabsTrigger>
                <TabsTrigger value="export">Export Results</TabsTrigger>
              </TabsList>

              <TabsContent value="recommendations" className="space-y-4">
                <Card>
                  <CardHeader>
                    <CardTitle>All Recommendations</CardTitle>
                    <CardDescription>Prioritized suggestions from backend analysis</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    {result.modules
                      .flatMap((module) => module.recommendations)
                      .map((rec, index) => (
                        <div key={index} className="border rounded-lg p-4">
                          <div className="flex items-start justify-between mb-2">
                            <h4 className="font-semibold">{rec.title}</h4>
                            <Badge variant={getPriorityColor(rec.priority)}>{rec.priority}</Badge>
                          </div>
                          <p className="text-gray-600 mb-3">{rec.message}</p>
                          {rec.codeSnippet && (
                            <div className="bg-gray-100 rounded p-3 mb-3">
                              <code className="text-sm">{rec.codeSnippet}</code>
                            </div>
                          )}
                          {rec.docLink && (
                            <a
                              href={rec.docLink}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-blue-600 hover:underline text-sm flex items-center"
                            >
                              Learn more <ExternalLink className="h-3 w-3 ml-1" />
                            </a>
                          )}
                        </div>
                      ))}
                  </CardContent>
                </Card>
              </TabsContent>

              <TabsContent value="modules" className="space-y-4">
                {result.modules.map((module) => (
                  <Card key={module.name}>
                    <CardHeader>
                      <div className="flex items-center justify-between">
                        <CardTitle className="flex items-center">
                          {module.name === "SEO & Metadata" && <Search className="h-5 w-5 mr-2" />}
                          {module.name === "Performance" && <Zap className="h-5 w-5 mr-2" />}
                          {module.name === "Security" && <Shield className="h-5 w-5 mr-2" />}
                          {module.name === "Mobile Friendliness" && <Smartphone className="h-5 w-5 mr-2" />}
                          {module.name.includes("Crawl") && <Globe className="h-5 w-5 mr-2" />}
                          {module.name}
                        </CardTitle>
                        <div className="text-right">
                          <div className={`text-2xl font-bold ${getScoreColor(module.score)}`}>{module.score}%</div>
                          <div className="text-sm text-gray-500">{getScoreLabel(module.score)}</div>
                        </div>
                      </div>
                      <CardDescription>{module.description}</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <Progress value={module.score} className="mb-4" />
                      <p className="text-gray-600 mb-4">{module.explanation}</p>
                      {module.recommendations.length > 0 && (
                        <div className="space-y-2">
                          <h5 className="font-semibold text-sm">Module Recommendations:</h5>
                          {module.recommendations.map((rec, index) => (
                            <div key={index} className="text-sm border-l-2 border-blue-200 pl-3">
                              <div className="flex items-center gap-2">
                                <Badge variant={getPriorityColor(rec.priority)} className="text-xs">
                                  {rec.priority}
                                </Badge>
                                <span className="font-medium">{rec.title}</span>
                              </div>
                              <p className="text-gray-600 mt-1">{rec.message}</p>
                            </div>
                          ))}
                        </div>
                      )}
                    </CardContent>
                  </Card>
                ))}
              </TabsContent>

              <TabsContent value="export">
                <Card>
                  <CardHeader>
                    <CardTitle className="flex items-center">
                      <Download className="h-5 w-5 mr-2" />
                      Export Analysis Results
                    </CardTitle>
                    <CardDescription>Download your backend analysis results</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ExportManager result={result} />

                    <Alert className="mt-6">
                      <CheckCircle className="h-4 w-4" />
                      <AlertDescription>
                        Analysis completed successfully using backend API. All data is sourced from the Python analysis
                        engine.
                      </AlertDescription>
                    </Alert>
                  </CardContent>
                </Card>
              </TabsContent>
            </Tabs>
          </div>
        )}

        {/* No Results State */}
        {!result && !isAnalyzing && !error && (
          <Card className="max-w-2xl mx-auto">
            <CardContent className="text-center py-12">
              <Globe className="h-16 w-16 text-gray-400 mx-auto mb-4" />
              <h3 className="text-lg font-semibold text-gray-600 mb-2">Ready to Analyze</h3>
              <p className="text-gray-500">Enter a website URL above to get started with backend-powered analysis</p>
            </CardContent>
          </Card>
=======
        {/* Results */}
        {result && (
          <div className="space-y-8">
            {/* Validation Status */}
            {result.validationResult && (
              <Card
                className={
                  result.validationResult.isValid ? "border-green-200 bg-green-50" : "border-red-200 bg-red-50"
                }
              >
                <CardHeader>
                  <CardTitle className="flex items-center">
                    {result.validationResult.isValid ? (
                      <CheckCircle className="h-5 w-5 mr-2 text-green-600" />
                    ) : (
                      <XCircle className="h-5 w-5 mr-2 text-red-600" />
                    )}
                    Website Validation Status
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <p className="text-sm font-medium">Legitimacy</p>
                      <p className={result.validationResult.isValid ? "text-green-600" : "text-red-600"}>
                        {result.validationResult.isValid ? "Verified Legitimate" : "Failed Validation"}
                      </p>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Confidence</p>
                      <p className="font-semibold">{((result.confidence || 0) * 100).toFixed(1)}%</p>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Status</p>
                      <p className="font-semibold">{result.validationResult.statusCode || "N/A"}</p>
                    </div>
                  </div>
                  {result.validationResult.details && (
                    <p className="mt-3 text-sm text-gray-600">{result.validationResult.details}</p>
                  )}
                  {result.validationResult.googleResults && result.validationResult.googleResults.length > 0 && (
                    <div className="mt-4">
                      <p className="text-sm font-medium mb-2">Google Search Results Found:</p>
                      <div className="space-y-2">
                        {result.validationResult.googleResults.slice(0, 3).map((searchResult, index) => (
                          <div key={index} className="text-xs bg-white p-2 rounded border">
                            <p className="font-medium">{searchResult.title}</p>
                            <p className="text-gray-600 truncate">{searchResult.snippet}</p>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>
            )}

            {/* Only show analysis results if validation passed */}
            {result.validationResult?.isValid && (result.overallScore || 0) > 0 && (
              <>
                {/* Overview */}
                <Card>
                  <CardHeader>
                    <CardTitle className="flex items-center justify-between">
                      <span>Verified Website Analysis</span>
                      <Badge variant="outline" className="text-green-600">
                        <ShieldCheck className="h-3 w-3 mr-1" />
                        {result.model_version}
                      </Badge>
                    </CardTitle>
                    <CardDescription>
                      Analyzed: {result.url} • {new Date(result.timestamp).toLocaleString()}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                      {/* Overall Score */}
                      <div className="text-center">
                        <CircularScore score={result.overallScore || 0} size={120} />
                        <h3 className="font-semibold mt-2">Website Health</h3>
                        <p className={`text-sm ${getScoreColor(result.overallScore || 0)}`}>{result.label}</p>
                        <p className="text-xs text-gray-500 mt-1">
                          Confidence: {((result.confidence || 0) * 100).toFixed(1)}%
                        </p>
                      </div>

                      {/* Module Scores */}
                      {result.modules.slice(0, 3).map((module) => (
                        <div key={module.name} className="text-center">
                          <CircularScore score={module.score || 0} size={80} />
                          <h4 className="font-medium mt-2 text-sm">{module.name}</h4>
                          <p className={`text-xs ${getScoreColor(module.score || 0)}`}>
                            {getScoreLabel(module.score || 0)}
                          </p>
                        </div>
                      ))}
                    </div>

                    <Separator className="my-6" />

                    {/* Key Metrics */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                      <div>
                        <p className="text-gray-600">Overall Score</p>
                        <p className="font-semibold">{result.overallScore || 0}%</p>
                      </div>
                      <div>
                        <p className="text-gray-600">Validation</p>
                        <p className="font-semibold text-green-600">Google Verified</p>
                      </div>
                      <div>
                        <p className="text-gray-600">Analysis Time</p>
                        <p className="font-semibold">{(result.analysis_time || 0).toFixed(2)}s</p>
                      </div>
                      <div>
                        <p className="text-gray-600">Status Code</p>
                        <p className="font-semibold">{result.features?.status_code || "N/A"}</p>
                      </div>
                    </div>

                    {result.features?.ssl_certificate_valid && (
                      <div className="mt-4">
                        <Badge variant="outline" className="text-green-600">
                          <Shield className="h-3 w-3 mr-1" />
                          HTTPS Secured
                        </Badge>
                      </div>
                    )}

                    {/* Quick Stats */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6 text-sm">
                      <div>
                        <p className="text-gray-600">Page Load Time</p>
                        <p className="font-semibold">{(result.features?.page_load_time || 0).toFixed(2)}s</p>
                      </div>
                      <div>
                        <p className="text-gray-600">Word Count</p>
                        <p className="font-semibold">{(result.features?.word_count || 0).toLocaleString()}</p>
                      </div>
                      <div>
                        <p className="text-gray-600">Images</p>
                        <p className="font-semibold">{result.features?.images_count || 0}</p>
                      </div>
                      <div>
                        <p className="text-gray-600">Internal Links</p>
                        <p className="font-semibold">{result.features?.internal_links_count || 0}</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                {/* Detailed Results */}
                <Tabs defaultValue="recommendations" className="w-full">
                  <TabsList className="grid w-full grid-cols-3">
                    <TabsTrigger value="recommendations">Recommendations</TabsTrigger>
                    <TabsTrigger value="modules">Technical Details</TabsTrigger>
                    <TabsTrigger value="export">Export & Reports</TabsTrigger>
                  </TabsList>

                  <TabsContent value="recommendations" className="space-y-4">
                    <Card>
                      <CardHeader>
                        <CardTitle>Recommendations ({result.recommendations.length})</CardTitle>
                        <CardDescription>
                          Prioritized suggestions to improve your verified website's performance and SEO
                        </CardDescription>
                      </CardHeader>
                      <CardContent className="space-y-4">
                        {result.recommendations.map((rec, index) => (
                          <div key={index} className="border rounded-lg p-4">
                            <div className="flex items-start justify-between mb-2">
                              <h4 className="font-semibold">{rec.title}</h4>
                              <Badge variant={getPriorityColor(rec.priority)}>{rec.priority}</Badge>
                            </div>
                            <p className="text-gray-600 mb-3">{rec.message}</p>
                            {rec.codeSnippet && (
                              <div className="bg-gray-100 rounded p-3 mb-3">
                                <code className="text-sm">{rec.codeSnippet}</code>
                              </div>
                            )}
                            {rec.docLink && (
                              <a
                                href={rec.docLink}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="text-blue-600 hover:underline text-sm flex items-center"
                              >
                                Learn more <ExternalLink className="h-3 w-3 ml-1" />
                              </a>
                            )}
                          </div>
                        ))}
                      </CardContent>
                    </Card>
                  </TabsContent>

                  <TabsContent value="modules" className="space-y-4">
                    {result.modules.map((module) => (
                      <Card key={module.name}>
                        <CardHeader>
                          <div className="flex items-center justify-between">
                            <CardTitle className="flex items-center">
                              {module.name === "SEO & Metadata" && <Search className="h-5 w-5 mr-2" />}
                              {module.name === "Performance" && <Zap className="h-5 w-5 mr-2" />}
                              {module.name === "Security" && <Shield className="h-5 w-5 mr-2" />}
                              {module.name === "Mobile Friendliness" && <Smartphone className="h-5 w-5 mr-2" />}
                              {module.name === "Crawlability" && <Globe className="h-5 w-5 mr-2" />}
                              {module.name}
                            </CardTitle>
                            <div className="text-right">
                              <div className={`text-2xl font-bold ${getScoreColor(module.score || 0)}`}>
                                {module.score || 0}%
                              </div>
                              <div className="text-sm text-gray-500">{getScoreLabel(module.score || 0)}</div>
                            </div>
                          </div>
                          <CardDescription>{module.description}</CardDescription>
                        </CardHeader>
                        <CardContent>
                          <Progress value={module.score || 0} className="mb-4" />
                          <p className="text-gray-600 mb-4">{module.explanation}</p>
                          {module.recommendations.length > 0 && (
                            <div className="space-y-2">
                              <h5 className="font-semibold text-sm">Specific Recommendations:</h5>
                              {module.recommendations.map((rec, index) => (
                                <div key={index} className="text-sm border-l-2 border-blue-200 pl-3">
                                  <div className="flex items-center gap-2">
                                    <Badge variant={getPriorityColor(rec.priority)} className="text-xs">
                                      {rec.priority}
                                    </Badge>
                                    <span className="font-medium">{rec.title}</span>
                                  </div>
                                  <p className="text-gray-600 mt-1">{rec.message}</p>
                                </div>
                              ))}
                            </div>
                          )}
                        </CardContent>
                      </Card>
                    ))}
                  </TabsContent>

                  <TabsContent value="export">
                    <Card>
                      <CardHeader>
                        <CardTitle className="flex items-center">
                          <Download className="h-5 w-5 mr-2" />
                          Export Verified Analysis
                        </CardTitle>
                        <CardDescription>Download your verified website analysis results</CardDescription>
                      </CardHeader>
                      <CardContent>
                        <Suspense fallback={<div>Loading export options...</div>}>
                          <ExportManager result={result} />
                        </Suspense>

                        <Alert className="mt-6">
                          <CheckCircle className="h-4 w-4" />
                          <AlertDescription>
                            Analysis completed successfully on verified legitimate website. All data is based on
                            real-time analysis with Google verification.
                          </AlertDescription>
                        </Alert>
                      </CardContent>
                    </Card>
                  </TabsContent>
                </Tabs>
              </>
            )}
          </div>
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        )}
      </div>
    </div>
  )
}
