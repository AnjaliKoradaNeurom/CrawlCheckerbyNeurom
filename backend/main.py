<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime
import asyncio
import logging
import os

from models.schemas import AnalysisRequest, AnalysisResult, ModuleResult, Recommendation
from core.validation import URLValidator # Import URLValidator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Neurom Website Analyzer API", version="1.0.0")

# CORS middleware - Allow all origins for development
=======
"""
Main FastAPI application with comprehensive web audit functionality
"""

import asyncio
import logging
import time
import os
import sys
import io
from contextlib import asynccontextmanager
from typing import Dict, Any, List, Optional
from datetime import datetime
import json
import uuid
import statistics
from collections import defaultdict

from fastapi import FastAPI, HTTPException, Request, BackgroundTasks, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.security import HTTPBearer
from pydantic import HttpUrl, ValidationError
import uvicorn
from dotenv import load_dotenv

# Import our modules
from core.crawler import WebCrawler
from core.feature_extractor import FeatureExtractor
from core.ai_analyzer import AIAnalyzer
from core.rate_limiter import RateLimiter
from core.export_manager import ExportManager
from core.validation import URLValidator
from models.schemas import (
    AnalysisResult, BatchAnalysisRequest, BatchAnalysisResult,
    HealthCheckResult, ValidationResult, CrawlabilityFeatures
)
from analyzers.normalized_crawlability_analyzer import NormalizedCrawlabilityAnalyzer

# Load environment variables
load_dotenv()

# Configure logging with UTF-8 encoding
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Global components
crawler = None
feature_extractor = None
ai_analyzer = None
rate_limiter = None
export_manager = None
url_validator = None
normalized_analyzer = None

# Background tasks storage
background_tasks_storage = {}

# Global score tracking for consistency monitoring
score_history = defaultdict(list)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    global crawler, feature_extractor, ai_analyzer, rate_limiter, export_manager, url_validator, normalized_analyzer
    
    logger.info("🚀 Starting Neurom AI Website Analyzer...")
    
    try:
        # Initialize components
        crawler = WebCrawler()
        feature_extractor = FeatureExtractor()
        ai_analyzer = AIAnalyzer()
        rate_limiter = RateLimiter(max_requests=100, window_seconds=3600)
        export_manager = ExportManager()
        url_validator = URLValidator()
        normalized_analyzer = NormalizedCrawlabilityAnalyzer()
        
        # Load AI model
        await ai_analyzer.load_model()
        
        logger.info("✅ All components initialized successfully")
        
        yield
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize components: {e}")
        raise
    finally:
        logger.info("🛑 Shutting down Neurom AI Website Analyzer...")

# Create FastAPI app
app = FastAPI(
    title="Neurom AI Website Analyzer",
    description="Production-grade website crawlability and SEO analysis tool with AI-powered insights and environment normalization",
    version="2.0.0-normalized",
    lifespan=lifespan
)

# CORS middleware
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Instantiate URLValidator globally for efficiency
url_validator = URLValidator()

def generate_mock_analysis(url: str) -> AnalysisResult:
    """Generate mock analysis results for testing"""
    
    url_hash = hash(url) % 100
    base_score = 60 + (url_hash % 40)
    
    modules = [
        ModuleResult(
            name="SEO & Metadata",
            score=min(100, base_score + 5),
            description="Search engine optimization and meta tags analysis",
            explanation="SEO analysis shows good optimization with proper meta tags and content structure.",
            recommendations=[
                Recommendation(
                    priority="Medium",
                    title="Optimize Meta Description",
                    message="Consider improving meta description length for better search results display.",
                    code_snippet='<meta name="description" content="Optimized description (120-160 chars)">',
                    doc_link="https://developers.google.com/search/docs/appearance/snippet"
                )
            ]
        ),
        ModuleResult(
            name="Performance",
            score=min(100, base_score - 10),
            description="Website speed and performance metrics",
            explanation="Performance analysis shows room for improvement in loading speed and optimization.",
            recommendations=[
                Recommendation(
                    priority="High",
                    title="Optimize Images",
                    message="Compress and properly format images to reduce loading times.",
                    code_snippet='<img src="image.webp" alt="Description" loading="lazy">',
                    doc_link="https://web.dev/fast/#optimize-your-images"
                )
            ]
        ),
        ModuleResult(
            name="Security",
            score=min(100, base_score + 15),
            description="HTTPS and security implementation",
            explanation="Security analysis shows good HTTPS implementation with room for header improvements.",
            recommendations=[
                Recommendation(
                    priority="Medium",
                    title="Add Security Headers",
                    message="Implement additional security headers for better protection.",
                    code_snippet="Strict-Transport-Security: max-age=31536000; includeSubDomains",
                    doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#security"
                )
            ]
        ),
        ModuleResult(
            name="Mobile Friendliness",
            score=min(100, base_score + 8),
            description="Mobile device compatibility and usability",
            explanation="Mobile analysis shows good responsive design with minor optimization opportunities.",
            recommendations=[
                Recommendation(
                    priority="Low",
                    title="Optimize Touch Targets",
                    message="Ensure all interactive elements are properly sized for touch interaction.",
                    code_snippet='.touch-target { min-height: 44px; min-width: 44px; }',
                    doc_link="https://web.dev/accessible-tap-targets/"
                )
            ]
        ),
        ModuleResult(
            name="Crawlability",
            score=min(100, base_score - 5),
            description="Search engine crawling accessibility",
            explanation="Crawlability analysis shows good structure with some areas for improvement.",
            recommendations=[
                Recommendation(
                    priority="Medium",
                    title="Optimize Robots.txt",
                    message="Review and optimize robots.txt file for better crawling guidance.",
                    code_snippet="User-agent: *\nAllow: /\nSitemap: https://yoursite.com/sitemap.xml",
                    doc_link="https://developers.google.com/search/docs/crawling-indexing/robots/intro"
                )
            ]
        ),
        ModuleResult(
            name="Indexing",
            score=min(100, base_score + 2),
            description="Search engine indexing optimization",
            explanation="Indexing analysis shows proper setup with opportunities for canonical tag optimization.",
            recommendations=[
                Recommendation(
                    priority="Medium",
                    title="Add Canonical Tags",
                    message="Implement canonical tags to prevent duplicate content issues.",
                    code_snippet='<link rel="canonical" href="https://example.com/preferred-url">',
                    doc_link="https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls"
                )
            ]
        )
    ]
    
    overall_score = sum(m.score for m in modules) // len(modules)
    
    return AnalysisResult(
        url=url,
        timestamp=datetime.now().isoformat(),
        overall_score=overall_score,
        modules=modules,
        analysis_time=2.5
    )

@app.get("/")
async def root():
    return {
        "message": "Neurom Website Analyzer API", 
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "analyze": "POST /analyze",
            "health": "GET /health",
            "docs": "GET /docs"
        }
    }

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_website(request: AnalysisRequest):
    try:
        logger.info(f"Analyzing website: {request.url}")
        
        # Use the comprehensive URLValidator for pre-check
        validation_result = await url_validator.validate_url(request.url)
        
        if not validation_result.is_valid:
            raise HTTPException(
                status_code=400,
                detail=validation_result.error or "Website validation failed. Analysis aborted."
            )

        # Simulate analysis time
        await asyncio.sleep(1)
        
        # Generate mock analysis
        result = generate_mock_analysis(request.url)
        
        logger.info(f"Analysis completed for {request.url} with score {result.overall_score}%")
        return result
        
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Analysis failed for {request.url}: {e}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Neurom Website Analyzer API...")
    print("📊 API Documentation: http://localhost:8000/docs")
    print("🌐 API Endpoint: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
=======
# Security
security = HTTPBearer(auto_error=False)

def get_client_ip(request: Request) -> str:
    """Get client IP address"""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host

async def check_rate_limit(request: Request):
    """Check rate limiting"""
    client_ip = get_client_ip(request)
    
    if not rate_limiter.allow_request(client_ip):
        raise HTTPException(
            status_code=429,
            detail={
                "error": "Rate limit exceeded",
                "message": "Too many requests. Please try again later.",
                "retry_after": 3600
            }
        )
    
    return client_ip

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "message": "Neurom AI Website Analyzer API",
        "version": "2.0.0-normalized",
        "status": "online",
        "documentation": "/docs",
        "features": [
            "Environment normalization for consistent scoring",
            "Standardized request headers",
            "Load time normalization",
            "Multiple-attempt median scoring"
        ]
    }

@app.get("/health", response_model=HealthCheckResult)
async def health_check():
    """Health check endpoint"""
    try:
        components = {
            "crawler": crawler is not None,
            "feature_extractor": feature_extractor is not None,
            "ai_analyzer": ai_analyzer is not None and ai_analyzer.is_loaded,
            "rate_limiter": rate_limiter is not None,
            "export_manager": export_manager is not None,
            "url_validator": url_validator is not None,
            "normalized_analyzer": normalized_analyzer is not None
        }
        
        all_healthy = all(components.values())
        
        return HealthCheckResult(
            status="healthy" if all_healthy else "degraded",
            timestamp=datetime.now().isoformat(),
            version="2.0.0-normalized",
            components=components,
            system_info={
                "python_version": sys.version,
                "platform": sys.platform,
                "openai_available": bool(os.getenv('OPENAI_API_KEY')),
                "google_api_available": bool(os.getenv('GOOGLE_API_KEY')),
                "lighthouse_available": bool(os.getenv('LIGHTHOUSE_PATH')),
                "normalization_enabled": True
            }
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=500, detail="Health check failed")

@app.post("/validate", response_model=ValidationResult)
async def validate_url(
    url: str,
    client_ip: str = Depends(check_rate_limit)
):
    """Validate URL and check if it's accessible"""
    try:
        logger.info(f"🔍 Validating URL: {url} from IP: {client_ip}")
        
        result = await url_validator.validate_url(url)
        
        logger.info(f"✅ URL validation completed for: {url}")
        return result
        
    except Exception as e:
        logger.error(f"❌ URL validation failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_website(
    url: str,
    include_lighthouse: bool = False,
    use_normalized: bool = True,
    client_ip: str = Depends(check_rate_limit)
):
    """Analyze a single website with optional environment normalization"""
    start_time = time.time()
    
    try:
        if use_normalized:
            logger.info(f"🔧 Starting NORMALIZED analysis for: {url} from IP: {client_ip}")
            
            # Use normalized analyzer for consistent results
            normalized_result = await normalized_analyzer.analyze(url)
            
            # Convert to AnalysisResult format
            result = AnalysisResult(
                url=url,
                timestamp=datetime.now().isoformat(),
                crawlability_score=normalized_result.score,
                confidence=normalized_result.confidence,
                label=self._get_score_label(normalized_result.score),
                features={
                    "normalization_applied": True,
                    "analysis_method": "normalized",
                    "consistency_level": "high"
                },
                recommendations=[rec.dict() for rec in normalized_result.recommendations],
                analysis_time=time.time() - start_time,
                model_version="2.0.0-normalized",
                backend_status="online"
            )
            
            # Track score for consistency monitoring
            score_history[url].append(result.crawlability_score)
            
            # Log score statistics if we have multiple measurements
            if len(score_history[url]) > 1:
                scores = score_history[url][-10:]  # Last 10 scores
                avg_score = statistics.mean(scores)
                std_dev = statistics.stdev(scores) if len(scores) > 1 else 0
                min_score = min(scores)
                max_score = max(scores)
                variance = max_score - min_score
                
                logger.info(f"📊 Score consistency for {url}: avg={avg_score:.1f}, std_dev={std_dev:.2f}, variance={variance}")
                
                # Alert if high variance (should be rare with normalization)
                if std_dev > 3.0:
                    logger.warning(f"⚠️ Unexpected score variance detected for {url}: {std_dev:.2f}")
                else:
                    logger.info(f"✅ Good score consistency maintained: ±{std_dev:.2f}")
            
            logger.info(f"✅ Normalized analysis completed for {url} in {result.analysis_time:.2f}s - Score: {result.crawlability_score}")
            
        else:
            logger.info(f"🔍 Starting STANDARD analysis for: {url} from IP: {client_ip}")
            
            # Use original analysis method (for comparison)
            validation_result = await url_validator.validate_url(url)
            
            if not validation_result.is_valid:
                return AnalysisResult(
                    url=url,
                    timestamp=datetime.now().isoformat(),
                    crawlability_score=0.0,
                    confidence=0.0,
                    label="Invalid URL",
                    features={"analysis_method": "standard"},
                    recommendations=[{
                        "priority": "High",
                        "title": "Invalid URL",
                        "message": validation_result.error or "URL is not accessible",
                        "impact_score": 0
                    }],
                    analysis_time=time.time() - start_time,
                    model_version="2.0.0-standard",
                    backend_status="online"
                )
            
            # Use normalized URL
            normalized_url = validation_result.normalized_url or url
            
            # Crawl website
            crawl_result = await crawler.crawl_website(normalized_url)
            
            if not crawl_result.get('success', False):
                return AnalysisResult(
                    url=normalized_url,
                    timestamp=datetime.now().isoformat(),
                    crawlability_score=0.0,
                    confidence=0.0,
                    label="Crawl Failed",
                    features={"analysis_method": "standard"},
                    recommendations=[{
                        "priority": "High",
                        "title": "Website Inaccessible",
                        "message": crawl_result.get('error', 'Unable to access website'),
                        "impact_score": 0
                    }],
                    analysis_time=time.time() - start_time,
                    model_version="2.0.0-standard",
                    backend_status="online"
                )
            
            # Extract features
            features = await feature_extractor.extract_features(crawl_result)
            
            # Get additional data (robots.txt, sitemap)
            robots_result = await crawler.check_robots_txt(normalized_url)
            sitemap_result = await crawler.check_sitemap(normalized_url)
            
            features.robots_txt_exists = robots_result.get('exists', False)
            features.robots_txt_blocks_crawling = robots_result.get('blocks_crawling', False)
            features.sitemap_exists = sitemap_result.get('exists', False)
            
            # AI Analysis
            ai_result = await ai_analyzer.analyze_crawlability(features)
            
            # Prepare result
            analysis_time = time.time() - start_time
            
            result = AnalysisResult(
                url=normalized_url,
                timestamp=datetime.now().isoformat(),
                crawlability_score=ai_result.score,
                confidence=ai_result.confidence,
                label=ai_result.label,
                features={**features.dict(), "analysis_method": "standard"},
                recommendations=[rec.dict() for rec in ai_result.recommendations],
                analysis_time=analysis_time,
                model_version="2.0.0-standard",
                backend_status="online"
            )
            
            logger.info(f"✅ Standard analysis completed for {normalized_url} in {analysis_time:.2f}s - Score: {ai_result.score:.1f}%")
        
        return result
        
    except Exception as e:
        logger.error(f"❌ Analysis failed for {url}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

def _get_score_label(score: int) -> str:
    """Get label for score"""
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Fair"
    elif score >= 60:
        return "Poor"
    else:
        return "Critical"

@app.post("/analyze/batch", response_model=BatchAnalysisResult)
async def start_batch_analysis(
    request: BatchAnalysisRequest,
    background_tasks: BackgroundTasks,
    use_normalized: bool = True,
    client_ip: str = Depends(check_rate_limit)
):
    """Start batch analysis of multiple URLs with normalization option"""
    try:
        batch_id = str(uuid.uuid4())
        
        logger.info(f"🔄 Starting {'NORMALIZED' if use_normalized else 'STANDARD'} batch analysis {batch_id} for {len(request.urls)} URLs from IP: {client_ip}")
        
        # Initialize batch result
        batch_result = BatchAnalysisResult(
            batch_id=batch_id,
            status="processing",
            total_urls=len(request.urls),
            processed=0,
            failed=0,
            results=[],
            started_at=datetime.now()
        )
        
        # Store in memory (in production, use Redis or database)
        background_tasks_storage[batch_id] = batch_result
        
        # Start background processing
        background_tasks.add_task(
            process_batch_analysis,
            batch_id,
            [str(url) for url in request.urls],
            use_normalized
        )
        
        return batch_result
        
    except Exception as e:
        logger.error(f"❌ Batch analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analyze/batch/{batch_id}", response_model=BatchAnalysisResult)
async def get_batch_status(batch_id: str):
    """Get batch analysis status"""
    if batch_id not in background_tasks_storage:
        raise HTTPException(status_code=404, detail="Batch not found")
    
    return background_tasks_storage[batch_id]

async def process_batch_analysis(batch_id: str, urls: List[str], use_normalized: bool = True):
    """Process batch analysis in background"""
    try:
        batch_result = background_tasks_storage[batch_id]
        
        for url in urls:
            try:
                if use_normalized:
                    # Use normalized analyzer
                    normalized_result = await normalized_analyzer.analyze(url)
                    
                    result = AnalysisResult(
                        url=url,
                        timestamp=datetime.now().isoformat(),
                        crawlability_score=normalized_result.score,
                        confidence=normalized_result.confidence,
                        label=_get_score_label(normalized_result.score),
                        features={"analysis_method": "normalized"},
                        recommendations=[rec.dict() for rec in normalized_result.recommendations],
                        analysis_time=0.0,
                        model_version="2.0.0-normalized",
                        backend_status="online"
                    )
                    
                    batch_result.results.append(result)
                    batch_result.processed += 1
                    
                else:
                    # Use standard analyzer
                    validation_result = await url_validator.validate_url(url)
                    
                    if validation_result.is_valid:
                        normalized_url = validation_result.normalized_url or url
                        crawl_result = await crawler.crawl_website(normalized_url)
                        
                        if crawl_result.get('success', False):
                            features = await feature_extractor.extract_features(crawl_result)
                            ai_result = await ai_analyzer.analyze_crawlability(features)
                            
                            result = AnalysisResult(
                                url=normalized_url,
                                timestamp=datetime.now().isoformat(),
                                crawlability_score=ai_result.score,
                                confidence=ai_result.confidence,
                                label=ai_result.label,
                                features={**features.dict(), "analysis_method": "standard"},
                                recommendations=[rec.dict() for rec in ai_result.recommendations],
                                analysis_time=0.0,
                                model_version="2.0.0-standard",
                                backend_status="online"
                            )
                            
                            batch_result.results.append(result)
                            batch_result.processed += 1
                        else:
                            batch_result.failed += 1
                    else:
                        batch_result.failed += 1
                
            except Exception as e:
                logger.error(f"❌ Failed to analyze {url} in batch: {str(e)}")
                batch_result.failed += 1
        
        # Mark as completed
        batch_result.status = "completed"
        batch_result.completed_at = datetime.now()
        
        logger.info(f"✅ Batch analysis {batch_id} completed: {batch_result.processed} processed, {batch_result.failed} failed")
        
    except Exception as e:
        logger.error(f"❌ Batch processing failed: {str(e)}")
        batch_result.status = "failed"

@app.post("/export/pdf")
async def export_pdf(
    analysis_data: Dict[str, Any],
    client_ip: str = Depends(check_rate_limit)
):
    """Export analysis results as PDF"""
    try:
        logger.info(f"📄 Generating PDF export from IP: {client_ip}")
        
        pdf_data = await export_manager.generate_pdf_report(analysis_data)
        
        return StreamingResponse(
            io.BytesIO(pdf_data),
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=website_analysis.pdf"}
        )
        
    except Exception as e:
        logger.error(f"❌ PDF export failed: {str(e)}")
        raise HTTPException(status_code=500, detail="PDF export failed")

@app.post("/export/csv")
async def export_csv(
    analysis_data: Dict[str, Any],
    client_ip: str = Depends(check_rate_limit)
):
    """Export analysis results as CSV"""
    try:
        logger.info(f"📊 Generating CSV export from IP: {client_ip}")
        
        csv_data = await export_manager.generate_csv_report(analysis_data)
        
        return StreamingResponse(
            io.StringIO(csv_data),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=website_analysis.csv"}
        )
        
    except Exception as e:
        logger.error(f"❌ CSV export failed: {str(e)}")
        raise HTTPException(status_code=500, detail="CSV export failed")

@app.get("/stats")
async def get_stats():
    """Get API statistics including score consistency metrics"""
    try:
        stats = rate_limiter.get_stats()
        
        # Calculate score consistency statistics
        consistency_stats = {}
        for url, scores in score_history.items():
            if len(scores) > 1:
                avg_score = statistics.mean(scores)
                std_dev = statistics.stdev(scores)
                min_score = min(scores)
                max_score = max(scores)
                variance = max_score - min_score
                
                consistency_stats[url] = {
                    "measurements": len(scores),
                    "average_score": round(avg_score, 1),
                    "standard_deviation": round(std_dev, 2),
                    "variance": variance,
                    "consistency_rating": "excellent" if std_dev <= 2 else "good" if std_dev <= 5 else "poor"
                }
        
        return {
            "api_stats": stats,
            "background_tasks": len(background_tasks_storage),
            "system_status": "online",
            "version": "2.0.0-normalized",
            "score_consistency": consistency_stats,
            "normalization_enabled": True
        }
        
    except Exception as e:
        logger.error(f"❌ Stats retrieval failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Stats unavailable")

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    """Handle validation errors"""
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "details": exc.errors(),
            "message": "Please check your input data"
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions"""
    logger.error(f"❌ Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred",
            "request_id": str(uuid.uuid4())
        }
    )

if __name__ == "__main__":
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    logger.info(f"🚀 Starting Normalized Website Analyzer on {host}:{port}")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info" if not debug else "debug",
        access_log=True
    )
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
