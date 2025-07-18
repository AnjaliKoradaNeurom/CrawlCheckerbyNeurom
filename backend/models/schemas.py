<<<<<<< HEAD
"""Pydantic schemas for API request/response models"""
=======
"""
Pydantic schemas for API request/response models
"""

>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum

class PriorityLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

# Create alias for backward compatibility
Priority = PriorityLevel

<<<<<<< HEAD
# --- Existing models (for compatibility with current analyzers and main.py) ---
class Recommendation(BaseModel):
    priority: str # Keep as str for compatibility with existing analyzers
    title: str
    message: str
    code_snippet: Optional[str] = None
    doc_link: Optional[str] = None
    # Additional fields from normalized_crawlability_analyzer (kept optional for compatibility)
    category: Optional[str] = None
    impact: Optional[str] = None
    effort: Optional[str] = None
    resources: List[str] = []

class ModuleResult(BaseModel):
    name: str
    score: int
    description: str
    explanation: str
    recommendations: List[Recommendation]
    metadata: Optional[Dict] = None
    confidence: Optional[float] = None

class AnalysisRequest(BaseModel): # This is the simpler one used by main.py
    url: str

class AnalysisResult(BaseModel): # This is the simpler one used by main.py
    url: str
    timestamp: str
    overall_score: int
    modules: List[ModuleResult]
    analysis_time: float

# --- New, more comprehensive models (from your latest input) ---
class CrawlabilityFeatures(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    
    url: str
    status_code: int
    https_enabled: bool
    ssl_certificate_valid: bool
    html_size: int
    word_count: int
    page_load_time: float
=======
class Recommendation(BaseModel):
    priority: PriorityLevel
    title: str
    message: str
    impact_score: Optional[int] = Field(default=5, ge=1, le=10)
    code_snippet: Optional[str] = None
    doc_link: Optional[str] = None

class CrawlabilityFeatures(BaseModel):
    # Configure to allow model_ fields
    model_config = ConfigDict(protected_namespaces=())
    
    # Basic URL and response info
    url: str
    status_code: int
    
    # SSL and security
    https_enabled: bool
    ssl_certificate_valid: bool
    
    # Content metrics
    html_size: int
    word_count: int
    page_load_time: float
    
    # SEO elements
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    title_tag_present: bool = False
    title_length: int = 0
    meta_description_present: bool = False
    meta_description_length: int = 0
<<<<<<< HEAD
=======
    
    # Heading structure
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    h1_count: int = 0
    h1_text: str = ""
    h2_count: int = 0
    h3_count: int = 0
<<<<<<< HEAD
    internal_links_count: int = 0
    external_links_count: int = 0
    images_count: int = 0
    images_with_alt_count: int = 0
    external_scripts_count: int = 0
    external_stylesheets_count: int = 0
=======
    
    # Links
    internal_links_count: int = 0
    external_links_count: int = 0
    
    # Images
    images_count: int = 0
    images_with_alt_count: int = 0
    
    # Scripts and resources
    external_scripts_count: int = 0
    external_stylesheets_count: int = 0
    
    # Advanced SEO
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    canonical_tag_present: bool = False
    robots_txt_exists: bool = False
    robots_txt_blocks_crawling: bool = False
    sitemap_exists: bool = False
<<<<<<< HEAD
    mobile_friendly: bool = False
    viewport_configured: bool = False
    lazy_loading_images: int = 0
=======
    
    # Mobile and accessibility
    mobile_friendly: bool = False
    viewport_configured: bool = False
    lazy_loading_images: int = 0
    
    # Meta and structured data
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    meta_robots_noindex: bool = False
    structured_data_present: bool = False
    open_graph_present: bool = False
    open_graph_tags_count: int = 0
    twitter_cards_present: bool = False
<<<<<<< HEAD
    favicon_present: bool = False
    lang_attribute_present: bool = False
    charset_declared: bool = False
    inline_css_count: int = 0
    inline_js_count: int = 0
    deprecated_html_tags: int = 0
=======
    
    # Technical elements
    favicon_present: bool = False
    lang_attribute_present: bool = False
    charset_declared: bool = False
    
    # Code quality
    inline_css_count: int = 0
    inline_js_count: int = 0
    deprecated_html_tags: int = 0
    
    # Performance and optimization
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    broken_links_count: int = 0
    redirect_chains: int = 0
    compression_enabled: bool = False
    minified_resources: int = 0
    cache_headers_present: bool = False
<<<<<<< HEAD
    security_headers_count: int = 0
    mixed_content_issues: int = 0
    accessibility_score: float = 0.0
    performance_score: float = 0.0
    seo_score: float = 0.0
=======
    
    # Security
    security_headers_count: int = 0
    mixed_content_issues: int = 0
    
    # Calculated scores
    accessibility_score: float = 0.0
    performance_score: float = 0.0
    seo_score: float = 0.0
    
    # Additional features for extensibility
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    raw_features: Dict[str, Any] = {}

class AIAnalysisResult(BaseModel):
    score: float = Field(ge=0, le=100)
    confidence: float = Field(ge=0, le=1)
    label: str
<<<<<<< HEAD
    recommendations: List[Recommendation] # Using the combined Recommendation model
=======
    recommendations: List[Recommendation]
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    category_scores: Dict[str, float] = {}
    analysis_method: str = "rule_based"
    ai_explanation: Optional[str] = None

<<<<<<< HEAD
class AdvancedAnalysisRequest(BaseModel): # Renamed to avoid conflict
=======
class AnalysisRequest(BaseModel):
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    url: HttpUrl
    include_lighthouse: bool = False
    deep_crawl: bool = False

<<<<<<< HEAD
class ComprehensiveAnalysisResult(BaseModel): # Renamed to avoid conflict
=======
class AnalysisResult(BaseModel):
    # Configure to allow model_ fields
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    model_config = ConfigDict(protected_namespaces=())
    
    url: str
    timestamp: str
    crawlability_score: float = Field(ge=0, le=100)
    confidence: float = Field(ge=0, le=1)
    label: str
    features: Dict[str, Any]
<<<<<<< HEAD
    recommendations: List[Dict[str, Any]] # Keeping as Dict[str, Any] as per your input
    analysis_time: float
    model_version: str
=======
    recommendations: List[Dict[str, Any]]
    analysis_time: float
    model_version: str  # This will now work without warnings
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    backend_status: str = "online"

class BatchAnalysisRequest(BaseModel):
    urls: List[HttpUrl] = Field(min_length=1, max_length=100)
    include_lighthouse: bool = False

class BatchAnalysisResult(BaseModel):
    batch_id: str
<<<<<<< HEAD
    status: str
    total_urls: int
    processed: int = 0
    failed: int = 0
    results: List[AnalysisResult] = [] # Using the simpler AnalysisResult for batch compatibility
=======
    status: str  # "processing", "completed", "failed"
    total_urls: int
    processed: int = 0
    failed: int = 0
    results: List[AnalysisResult] = []
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    started_at: datetime
    completed_at: Optional[datetime] = None

class ValidationResult(BaseModel):
    is_valid: bool
    normalized_url: Optional[str] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
<<<<<<< HEAD
    redirect_chain: List[str] = [] # Changed to List[str] as per previous definition
=======
    redirect_chain: Optional[List[str]] = None
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b

class GoogleSearchResult(BaseModel):
    title: str
    link: str
    snippet: str
    position: int

class URLVerificationResult(BaseModel):
    is_real: bool
    is_indexed: bool
    search_results: List[GoogleSearchResult] = []
    verification_method: str
    confidence: float = Field(ge=0, le=1)

class HealthCheckResult(BaseModel):
<<<<<<< HEAD
    status: str
=======
    status: str  # "healthy", "degraded", "unhealthy"
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    timestamp: str
    version: str
    components: Dict[str, bool]
    system_info: Dict[str, Any] = {}
