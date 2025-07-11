export interface GoogleSearchResult {
  title: string
  link: string
  snippet: string
  position?: number
}

export interface ValidationResult {
  isValid: boolean
  normalizedUrl?: string
  error?: string
  confidence: number
  details?: string
  statusCode?: number
  googleResults?: GoogleSearchResult[]
  // New fields for enhanced validation
  dnsResolved?: boolean
  redirectChain?: string[]
  responseTime?: number
  validationMethod?: string
}

export interface Recommendation {
  priority: "High" | "Medium" | "Low"
  title: string
  message: string
  codeSnippet?: string
  docLink?: string
  // New field for categorization
  category?: string
}

export interface AuditModule {
  name: string
  score: number
  description: string
  explanation: string
  recommendations: Recommendation[]
  // New fields for enhanced module data
  analysisTime?: number
  dataSource?: string
  errorDetails?: string
}

export interface AuditResult {
  url: string
  timestamp: string
  overallScore: number
  modules: AuditModule[]
  crawlability_score: number
  confidence: number
  label: string
  features: Record<string, any>
  recommendations: Recommendation[]
  analysis_time: number
  model_version: string
  backend: string
  error?: string
  validationResult?: ValidationResult
  // New fields for enhanced audit results
  originalUrl?: string
  crawlStrategy?: string
  crawlTime?: number
  technicalDetails?: Record<string, any>
  healthStatus?: string
}

// New interfaces for enhanced functionality
export interface CrawlResult {
  success: boolean
  strategy?: string
  crawlTime?: number
  statusCode?: number
  htmlSize?: number
  wordCount?: number
  imagesCount?: number
  linksCount?: number
  robotsTxt?: Record<string, any>
  error?: string
}

export interface HealthCheckResult {
  status: "healthy" | "degraded" | "unhealthy"
  timestamp: string
  components: Record<string, any>
  overallHealth: string
  healthPercentage: number
  testResults?: any[]
}
