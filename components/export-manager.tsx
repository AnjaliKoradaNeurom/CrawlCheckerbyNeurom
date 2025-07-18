"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { FileText, Download } from "lucide-react"
<<<<<<< HEAD

// Updated interface to match backend response
interface AnalysisResult {
  url: string
  timestamp: string
  overall_score: number
  modules: Array<{
    name: string
    score: number
    description: string
    explanation: string
    recommendations: Array<{
      priority: string
      title: string
      message: string
      codeSnippet?: string
      docLink?: string
    }>
  }>
  analysis_time: number
}

interface ExportManagerProps {
  result: AnalysisResult
=======
import type { AuditResult } from "@/lib/types"

interface ExportManagerProps {
  result: AuditResult
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
}

export default function ExportManager({ result }: ExportManagerProps) {
  const [isExporting, setIsExporting] = useState(false)
  const [fileName, setFileName] = useState("")
  const [exportType, setExportType] = useState<"pdf" | "csv" | "json" | null>(null)

<<<<<<< HEAD
  // Only allow export if we have valid backend data
  if (!result || !result.url) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">No analysis data available for export</p>
        <p className="text-sm text-gray-400 mt-2">Complete an analysis first to enable export functionality</p>
      </div>
    )
  }

=======
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
  // Generate default filename based on URL and timestamp
  const generateDefaultFileName = (type: string) => {
    const domain = new URL(result.url).hostname.replace(/[^a-zA-Z0-9]/g, "_")
    const timestamp = new Date().toISOString().split("T")[0]
<<<<<<< HEAD
    return `backend_analysis_${domain}_${timestamp}.${type}`
  }

  // Export to JSON (native JavaScript) - only backend data
  const exportToJSON = (customFileName?: string) => {
    setIsExporting(true)
    try {
      // Create export object with only backend data
      const exportData = {
        metadata: {
          exportedAt: new Date().toISOString(),
          exportVersion: "2.0",
          tool: "Website Audit Tool - Backend API",
          dataSource: "Python FastAPI Backend",
=======
    return `website_audit_${domain}_${timestamp}.${type}`
  }

  // Export to PDF using jsPDF
  const exportToPDF = async (customFileName?: string) => {
    setIsExporting(true)
    try {
      // Dynamic import to reduce bundle size
      const { jsPDF } = await import("jspdf")
      const doc = new jsPDF()

      // Set up PDF styling
      const pageWidth = doc.internal.pageSize.getWidth()
      const margin = 20
      let yPosition = margin

      // Helper function to add text with word wrapping
      const addText = (text: string, fontSize = 12, isBold = false) => {
        doc.setFontSize(fontSize)
        if (isBold) doc.setFont(undefined, "bold")
        else doc.setFont(undefined, "normal")

        const lines = doc.splitTextToSize(text, pageWidth - 2 * margin)
        doc.text(lines, margin, yPosition)
        yPosition += lines.length * (fontSize * 0.4) + 5

        // Add new page if needed
        if (yPosition > doc.internal.pageSize.getHeight() - margin) {
          doc.addPage()
          yPosition = margin
        }
      }

      // Add header
      addText("Website Audit Report", 20, true)
      addText(`URL: ${result.url}`, 14, true)
      addText(`Generated: ${new Date(result.timestamp).toLocaleString()}`, 12)
      addText(`Overall Score: ${result.overallScore}% (${result.label})`, 14, true)
      yPosition += 10

      // Add validation status
      if (result.validationResult) {
        addText("Validation Status", 16, true)
        addText(`Status: ${result.validationResult.isValid ? "Verified Legitimate" : "Failed Validation"}`, 12)
        addText(`Confidence: ${(result.confidence * 100).toFixed(1)}%`, 12)
        if (result.validationResult.details) {
          addText(`Details: ${result.validationResult.details}`, 12)
        }
        yPosition += 10
      }

      // Add module scores
      addText("Module Analysis", 16, true)
      result.modules.forEach((module) => {
        addText(`${module.name}: ${module.score}%`, 12, true)
        addText(module.description, 10)
        addText(module.explanation, 10)
        yPosition += 5
      })

      // Add recommendations
      if (result.recommendations.length > 0) {
        yPosition += 10
        addText("Recommendations", 16, true)
        result.recommendations.forEach((rec, index) => {
          addText(`${index + 1}. [${rec.priority}] ${rec.title}`, 12, true)
          addText(rec.message, 10)
          if (rec.codeSnippet) {
            addText(`Code: ${rec.codeSnippet}`, 9)
          }
          yPosition += 5
        })
      }

      // Add technical details
      if (result.features) {
        yPosition += 10
        addText("Technical Details", 16, true)
        Object.entries(result.features).forEach(([key, value]) => {
          if (value !== null && value !== undefined) {
            addText(`${key.replace(/_/g, " ").toUpperCase()}: ${String(value)}`, 10)
          }
        })
      }

      // Save the PDF
      const filename = customFileName || generateDefaultFileName("pdf")
      doc.save(filename)
    } catch (error) {
      console.error("PDF export failed:", error)
      alert("Failed to export PDF. Please try again.")
    } finally {
      setIsExporting(false)
    }
  }

  // Export to CSV using Papa Parse
  const exportToCSV = async (customFileName?: string) => {
    setIsExporting(true)
    try {
      // Dynamic import to reduce bundle size
      const Papa = (await import("papaparse")).default

      // Prepare CSV data structure
      const csvData = []

      // Basic information
      csvData.push(["Field", "Value"])
      csvData.push(["URL", result.url])
      csvData.push(["Timestamp", result.timestamp])
      csvData.push(["Overall Score", `${result.overallScore}%`])
      csvData.push(["Label", result.label])
      csvData.push(["Confidence", `${(result.confidence * 100).toFixed(1)}%`])
      csvData.push(["Analysis Time", `${result.analysis_time}s`])
      csvData.push(["Model Version", result.model_version])
      csvData.push(["Backend", result.backend])
      csvData.push([""]) // Empty row for separation

      // Validation results
      if (result.validationResult) {
        csvData.push(["Validation Status", ""])
        csvData.push(["Is Valid", result.validationResult.isValid ? "Yes" : "No"])
        csvData.push(["Status Code", result.validationResult.statusCode || "N/A"])
        csvData.push(["Validation Details", result.validationResult.details || "N/A"])
        csvData.push([""]) // Empty row
      }

      // Module scores
      csvData.push(["Module Analysis", ""])
      csvData.push(["Module Name", "Score", "Description"])
      result.modules.forEach((module) => {
        csvData.push([module.name, `${module.score}%`, module.description])
      })
      csvData.push([""]) // Empty row

      // Recommendations
      if (result.recommendations.length > 0) {
        csvData.push(["Recommendations", ""])
        csvData.push(["Priority", "Title", "Message", "Code Snippet"])
        result.recommendations.forEach((rec) => {
          csvData.push([rec.priority, rec.title, rec.message, rec.codeSnippet || ""])
        })
        csvData.push([""]) // Empty row
      }

      // Technical features
      if (result.features) {
        csvData.push(["Technical Features", ""])
        csvData.push(["Feature", "Value"])
        Object.entries(result.features).forEach(([key, value]) => {
          if (value !== null && value !== undefined) {
            csvData.push([key.replace(/_/g, " ").toUpperCase(), String(value)])
          }
        })
      }

      // Convert to CSV and download
      const csv = Papa.unparse(csvData)
      const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" })
      const link = document.createElement("a")
      const url = URL.createObjectURL(blob)

      link.setAttribute("href", url)
      link.setAttribute("download", customFileName || generateDefaultFileName("csv"))
      link.style.visibility = "hidden"
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      URL.revokeObjectURL(url)
    } catch (error) {
      console.error("CSV export failed:", error)
      alert("Failed to export CSV. Please try again.")
    } finally {
      setIsExporting(false)
    }
  }

  // Export to JSON (native JavaScript)
  const exportToJSON = (customFileName?: string) => {
    setIsExporting(true)
    try {
      // Create a clean export object with all relevant data
      const exportData = {
        metadata: {
          exportedAt: new Date().toISOString(),
          exportVersion: "1.0",
          tool: "Website Audit Tool",
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        },
        analysis: {
          url: result.url,
          timestamp: result.timestamp,
<<<<<<< HEAD
          overall_score: result.overall_score,
          analysis_time: result.analysis_time,
        },
=======
          overallScore: result.overallScore,
          label: result.label,
          confidence: result.confidence,
          analysisTime: result.analysis_time,
          modelVersion: result.model_version,
          backend: result.backend,
        },
        validation: result.validationResult
          ? {
              isValid: result.validationResult.isValid,
              statusCode: result.validationResult.statusCode,
              details: result.validationResult.details,
              confidence: result.validationResult.confidence,
              googleResults: result.validationResult.googleResults || [],
            }
          : null,
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        modules: result.modules.map((module) => ({
          name: module.name,
          score: module.score,
          description: module.description,
          explanation: module.explanation,
          recommendations: module.recommendations,
        })),
<<<<<<< HEAD
        summary: {
          total_modules: result.modules.length,
          average_score: result.overall_score,
          total_recommendations: result.modules.reduce((sum, m) => sum + m.recommendations.length, 0),
        },
=======
        recommendations: result.recommendations,
        technicalFeatures: result.features || {},
        crawlabilityScore: result.crawlability_score,
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
      }

      // Convert to JSON string with pretty formatting
      const jsonString = JSON.stringify(exportData, null, 2)

      // Create and download the file
      const blob = new Blob([jsonString], { type: "application/json;charset=utf-8;" })
      const link = document.createElement("a")
      const url = URL.createObjectURL(blob)

      link.setAttribute("href", url)
      link.setAttribute("download", customFileName || generateDefaultFileName("json"))
      link.style.visibility = "hidden"
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      URL.revokeObjectURL(url)
    } catch (error) {
      console.error("JSON export failed:", error)
      alert("Failed to export JSON. Please try again.")
    } finally {
      setIsExporting(false)
    }
  }

  // Handle export with optional filename dialog
<<<<<<< HEAD
  const handleExport = (type: "json") => {
=======
  const handleExport = (type: "pdf" | "csv" | "json") => {
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    setExportType(type)
    setFileName(generateDefaultFileName(type))
  }

  // Execute the export
  const executeExport = () => {
    if (!exportType) return

    const customFileName = fileName.trim() || generateDefaultFileName(exportType)

    switch (exportType) {
<<<<<<< HEAD
=======
      case "pdf":
        exportToPDF(customFileName)
        break
      case "csv":
        exportToCSV(customFileName)
        break
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
      case "json":
        exportToJSON(customFileName)
        break
    }

    setExportType(null)
    setFileName("")
  }

  return (
    <div className="space-y-4">
<<<<<<< HEAD
      <div className="grid grid-cols-1 gap-4">
        {/* JSON Export Button - Only option since we only have backend data */}
=======
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* PDF Report Button */}
        <Dialog>
          <DialogTrigger asChild>
            <Button
              variant="outline"
              className="h-20 flex-col bg-transparent hover:bg-gray-50"
              onClick={() => handleExport("pdf")}
              disabled={isExporting}
            >
              <FileText className="h-6 w-6 mb-2 text-red-600" />
              <span className="font-medium">PDF Report</span>
              <span className="text-xs text-gray-500">Comprehensive analysis</span>
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Export PDF Report</DialogTitle>
              <DialogDescription>
                Generate a comprehensive PDF report of the website analysis including all modules, recommendations, and
                technical details.
              </DialogDescription>
            </DialogHeader>
            <div className="space-y-4">
              <div>
                <Label htmlFor="pdf-filename">File Name</Label>
                <Input
                  id="pdf-filename"
                  value={fileName}
                  onChange={(e) => setFileName(e.target.value)}
                  placeholder={generateDefaultFileName("pdf")}
                />
              </div>
            </div>
            <DialogFooter>
              <Button onClick={executeExport} disabled={isExporting}>
                {isExporting ? (
                  <>
                    <Download className="h-4 w-4 mr-2 animate-spin" />
                    Generating PDF...
                  </>
                ) : (
                  <>
                    <Download className="h-4 w-4 mr-2" />
                    Download PDF
                  </>
                )}
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>

        {/* CSV Data Button */}
        <Dialog>
          <DialogTrigger asChild>
            <Button
              variant="outline"
              className="h-20 flex-col bg-transparent hover:bg-gray-50"
              onClick={() => handleExport("csv")}
              disabled={isExporting}
            >
              <FileText className="h-6 w-6 mb-2 text-green-600" />
              <span className="font-medium">CSV Data</span>
              <span className="text-xs text-gray-500">Structured data export</span>
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>Export CSV Data</DialogTitle>
              <DialogDescription>
                Export all analysis data in CSV format for spreadsheet applications and data analysis tools.
              </DialogDescription>
            </DialogHeader>
            <div className="space-y-4">
              <div>
                <Label htmlFor="csv-filename">File Name</Label>
                <Input
                  id="csv-filename"
                  value={fileName}
                  onChange={(e) => setFileName(e.target.value)}
                  placeholder={generateDefaultFileName("csv")}
                />
              </div>
            </div>
            <DialogFooter>
              <Button onClick={executeExport} disabled={isExporting}>
                {isExporting ? (
                  <>
                    <Download className="h-4 w-4 mr-2 animate-spin" />
                    Generating CSV...
                  </>
                ) : (
                  <>
                    <Download className="h-4 w-4 mr-2" />
                    Download CSV
                  </>
                )}
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>

        {/* JSON Export Button */}
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        <Dialog>
          <DialogTrigger asChild>
            <Button
              variant="outline"
              className="h-20 flex-col bg-transparent hover:bg-gray-50"
              onClick={() => handleExport("json")}
              disabled={isExporting}
            >
              <FileText className="h-6 w-6 mb-2 text-blue-600" />
              <span className="font-medium">JSON Export</span>
<<<<<<< HEAD
              <span className="text-xs text-gray-500">Backend analysis data</span>
=======
              <span className="text-xs text-gray-500">Raw data format</span>
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
<<<<<<< HEAD
              <DialogTitle>Export Backend Analysis Data</DialogTitle>
              <DialogDescription>
                Export the complete backend analysis data in JSON format for developers and API integrations.
=======
              <DialogTitle>Export JSON Data</DialogTitle>
              <DialogDescription>
                Export the complete analysis data in JSON format for developers and API integrations.
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
              </DialogDescription>
            </DialogHeader>
            <div className="space-y-4">
              <div>
                <Label htmlFor="json-filename">File Name</Label>
                <Input
                  id="json-filename"
                  value={fileName}
                  onChange={(e) => setFileName(e.target.value)}
                  placeholder={generateDefaultFileName("json")}
                />
              </div>
            </div>
            <DialogFooter>
              <Button onClick={executeExport} disabled={isExporting}>
                {isExporting ? (
                  <>
                    <Download className="h-4 w-4 mr-2 animate-spin" />
                    Generating JSON...
                  </>
                ) : (
                  <>
                    <Download className="h-4 w-4 mr-2" />
                    Download JSON
                  </>
                )}
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      </div>

      {/* Export Status */}
      {isExporting && (
        <div className="text-center text-sm text-gray-600 flex items-center justify-center">
          <Download className="h-4 w-4 mr-2 animate-spin" />
<<<<<<< HEAD
          Preparing your backend data export...
=======
          Preparing your export...
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        </div>
      )}

      {/* Export Information */}
      <div className="text-xs text-gray-500 space-y-1">
        <p>
<<<<<<< HEAD
          <strong>JSON Export:</strong> Raw backend analysis data in JSON format
        </p>
        <p>
          <strong>Data Source:</strong> Python FastAPI backend - no client-side processing
        </p>
        <p>
          <strong>Note:</strong> PDF and CSV exports disabled - only backend data available
=======
          <strong>PDF Report:</strong> Complete formatted report with all analysis details
        </p>
        <p>
          <strong>CSV Data:</strong> Structured data suitable for Excel and data analysis
        </p>
        <p>
          <strong>JSON Export:</strong> Raw data format for developers and API integration
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        </p>
      </div>
    </div>
  )
}
