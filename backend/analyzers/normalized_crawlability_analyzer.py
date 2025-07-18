<<<<<<< HEAD
import asyncio
import logging
from typing import Dict, List
from models.schemas import Recommendation, ModuleResult

# Assuming EnvironmentNormalizer is a separate utility or part of this file
class EnvironmentNormalizer:
    """Mock EnvironmentNormalizer for demonstration."""
    async def normalized_crawl(self, url: str) -> Dict:
        # Simulate a successful crawl with some features
        return {
            'success': True,
            'url': url,
            'load_time': 1.5,
            'content': "<html><body><h1>Test Page</h1><p>This is some content.</p></body></html>",
            'headers': {},
            'content_hash': "mockhash",
            'normalized_load_time': 1.5,
            'raw_load_time': 1.5,
            'normalization_applied': True,
            'features': {
                'word_count': 500,
                'title_present': True,
                'title_length': 35,
                'meta_description_present': True,
                'meta_description_length': 150,
                'has_ssl': True,
                'has_viewport': True,
                'has_canonical': True,
                'h1_count': 1,
                'alt_ratio': 1.0,
                'internal_links_count': 5,
                'load_time': 1.5,
                'content_size': 100000,
                'load_time_score': 35,
                'content_size_score': 18,
                'content_quality_score': 30,
                'technical_quality_score': 30
            },
            'strategy': 'normalized'
        }

logger = logging.getLogger(__name__)

=======
"""
Normalized crawlability analyzer that provides consistent results across environments
"""

import asyncio
import logging
from typing import Dict, List
from pydantic import BaseModel

from core.environment_normalizer import EnvironmentNormalizer

logger = logging.getLogger(__name__)

class Recommendation(BaseModel):
    category: str
    title: str
    description: str
    priority: str
    impact: str
    effort: str
    resources: List[str] = []

class NormalizedModuleResult(BaseModel):
    name: str
    score: int
    description: str
    explanation: str
    recommendations: List[Recommendation]
    confidence: float = 0.95

>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
class NormalizedCrawlabilityAnalyzer:
    """
    Crawlability analyzer with environment normalization for consistent results
    """
    
    def __init__(self):
        self.normalizer = EnvironmentNormalizer()
    
<<<<<<< HEAD
    async def analyze(self, url: str) -> ModuleResult:
        # Pre-check: Google Search Indexing
        from core.validation import is_google_searchable # Import here to avoid circular dependency if EnvironmentNormalizer also imports it
        if not await is_google_searchable(url): # Await the async function
            return ModuleResult(
                name="Crawlability (Normalized)",
                score=0,
                description="Analysis aborted due to Google indexing check.",
                explanation="This website is not indexed by Google Search, so a full analysis cannot be performed by this module.",
                recommendations=[Recommendation(
                    priority="High",
                    title="Website Not Indexed by Google",
                    message="Ensure your website is properly indexed by Google Search. Check Google Search Console for issues.",
                    doc_link="https://developers.google.com/search/docs/basics/get-on-google"
                )]
            )

        try:
            logger.info(f"🔧 Starting normalized crawlability analysis for: {url}")
            
=======
    async def analyze(self, url: str) -> NormalizedModuleResult:
        """
        Perform normalized crawlability analysis
        """
        try:
            logger.info(f"🔧 Starting normalized crawlability analysis for: {url}")
            
            # Perform normalized crawl
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
            crawl_result = await self.normalizer.normalized_crawl(url)
            
            if not crawl_result['success']:
                return self._create_failed_result(url, crawl_result.get('error', 'Unknown error'))
            
<<<<<<< HEAD
            features = crawl_result['features']
            score = self._calculate_normalized_crawlability_score(features)
            
            recommendations = self._generate_normalized_recommendations(features, crawl_result)
            
            explanation = self._generate_explanation(score, features)
            
            result = ModuleResult(
=======
            # Calculate normalized score
            features = crawl_result['features']
            score = self._calculate_normalized_crawlability_score(features)
            
            # Generate recommendations
            recommendations = self._generate_normalized_recommendations(features, crawl_result)
            
            # Create explanation
            explanation = self._generate_explanation(score, features)
            
            result = NormalizedModuleResult(
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
                name="Crawlability (Normalized)",
                score=score,
                description="Search engine crawling accessibility with environment normalization",
                explanation=explanation,
                recommendations=recommendations,
                confidence=0.95
            )
            
            logger.info(f"✅ Normalized crawlability analysis completed - Score: {score}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Normalized crawlability analysis failed: {e}")
            return self._create_failed_result(url, str(e))
    
    def _calculate_normalized_crawlability_score(self, features: Dict) -> int:
        """Calculate crawlability score with normalization"""
        total_score = 0
        
<<<<<<< HEAD
        content_score = features.get('content_quality_score', 0)
        total_score += min(content_score, 35)
        
        technical_score = features.get('technical_quality_score', 0)
        total_score += min(technical_score, 40)
        
=======
        # Content Quality (35 points)
        content_score = features.get('content_quality_score', 0)
        total_score += min(content_score, 35)
        
        # Technical Quality (40 points) 
        technical_score = features.get('technical_quality_score', 0)
        total_score += min(technical_score, 40)
        
        # Performance (25 points)
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        load_time_score = features.get('load_time_score', 0)
        content_size_score = features.get('content_size_score', 0)
        performance_score = int(load_time_score * 0.6 + content_size_score * 0.4)
        total_score += min(performance_score, 25)
        
        return min(int(total_score), 100)
    
    def _generate_normalized_recommendations(self, features: Dict, crawl_result: Dict) -> List[Recommendation]:
        """Generate recommendations based on normalized analysis"""
        recommendations = []
        
<<<<<<< HEAD
=======
        # Content recommendations
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        if features.get('word_count', 0) < 300:
            recommendations.append(Recommendation(
                category="Content",
                title="Increase Content Length",
                description=f"Your page has {features.get('word_count', 0)} words. Add more quality content (aim for 300+ words) to improve search engine understanding.",
                priority="medium",
                impact="Improved search engine ranking and user engagement",
                effort="Medium - 1-2 hours",
                resources=["https://developers.google.com/search/docs/fundamentals/creating-helpful-content"]
            ))
        
        if not features.get('title_present', False):
            recommendations.append(Recommendation(
                category="SEO",
                title="Add Page Title",
                description="Your page is missing a title tag, which is crucial for SEO and search results.",
                priority="high",
                impact="Significantly improved search engine visibility",
                effort="Low - 5 minutes",
                resources=["https://developers.google.com/search/docs/appearance/title-link"]
            ))
        elif features.get('title_length', 0) < 30 or features.get('title_length', 0) > 60:
            recommendations.append(Recommendation(
                category="SEO", 
                title="Optimize Title Length",
                description=f"Title is {features.get('title_length', 0)} characters. Aim for 30-60 characters for optimal search results.",
                priority="medium",
                impact="Better click-through rates from search results",
                effort="Low - 10 minutes",
                resources=["https://developers.google.com/search/docs/appearance/title-link"]
            ))
        
        if not features.get('meta_description_present', False):
            recommendations.append(Recommendation(
                category="SEO",
                title="Add Meta Description", 
                description="Add a meta description to improve search engine results and click-through rates.",
                priority="high",
                impact="Improved search result appearance and CTR",
                effort="Low - 10 minutes",
                resources=["https://developers.google.com/search/docs/appearance/snippet"]
            ))
        
<<<<<<< HEAD
=======
        # Technical recommendations
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        if not features.get('has_ssl', False):
            recommendations.append(Recommendation(
                category="Security",
                title="Enable HTTPS",
                description="Secure your website with SSL certificate for better SEO and user trust.",
                priority="high", 
                impact="Improved search rankings and user security",
                effort="Medium - 1-2 hours",
                resources=["https://developers.google.com/search/docs/crawling-indexing/https"]
            ))
        
        if not features.get('has_viewport', False):
            recommendations.append(Recommendation(
                category="Mobile",
                title="Add Viewport Meta Tag",
                description="Add viewport meta tag for mobile responsiveness and better mobile search rankings.",
                priority="high",
                impact="Improved mobile user experience and rankings",
                effort="Low - 5 minutes", 
                resources=["https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing"]
            ))
        
        if features.get('h1_count', 0) == 0:
            recommendations.append(Recommendation(
                category="Content Structure",
                title="Add H1 Heading",
                description="Add an H1 heading to improve content structure and help search engines understand your page topic.",
                priority="medium",
                impact="Better content organization and SEO",
                effort="Low - 15 minutes",
                resources=["https://developers.google.com/search/docs/appearance/structured-data"]
            ))
        elif features.get('h1_count', 0) > 1:
            recommendations.append(Recommendation(
                category="Content Structure", 
                title="Use Single H1 Tag",
                description=f"Your page has {features.get('h1_count', 0)} H1 tags. Use only one H1 per page for better SEO.",
                priority="low",
                impact="Improved content hierarchy and SEO",
                effort="Low - 10 minutes",
                resources=["https://developers.google.com/search/docs/appearance/structured-data"]
            ))
        
<<<<<<< HEAD
=======
        # Performance recommendations
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        load_time = features.get('load_time', 0)
        if load_time > 3.0:
            recommendations.append(Recommendation(
                category="Performance",
                title="Improve Page Load Speed",
                description=f"Your page loads in {load_time:.2f} seconds. Optimize for faster loading (aim for under 2 seconds).",
                priority="medium",
                impact="Better user experience and search rankings",
                effort="High - 4-8 hours",
                resources=["https://developers.google.com/speed/docs/insights/rules"]
            ))
        
        content_size_mb = features.get('content_size', 0) / (1024 * 1024)
        if content_size_mb > 2.0:
            recommendations.append(Recommendation(
                category="Performance",
                title="Optimize Content Size",
                description=f"Your page is {content_size_mb:.2f}MB. Optimize images and content for faster loading.",
                priority="medium",
                impact="Faster page loading and better user experience", 
                effort="Medium - 2-4 hours",
                resources=["https://developers.google.com/speed/docs/insights/OptimizeImages"]
            ))
        
<<<<<<< HEAD
=======
        # Image accessibility
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        alt_ratio = features.get('alt_ratio', 0)
        if alt_ratio < 0.8:
            recommendations.append(Recommendation(
                category="Accessibility",
                title="Improve Image Alt Text",
                description=f"Only {alt_ratio*100:.0f}% of your images have alt text. Add descriptive alt text to all images.",
                priority="medium",
                impact="Better accessibility and SEO",
                effort="Medium - 1-2 hours",
                resources=["https://developers.google.com/search/docs/appearance/google-images"]
            ))
        
<<<<<<< HEAD
=======
        # Internal linking
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        internal_links = features.get('internal_links_count', 0)
        if internal_links < 3:
            recommendations.append(Recommendation(
                category="SEO",
                title="Improve Internal Linking",
                description=f"Your page has {internal_links} internal links. Add more internal links to help search engines discover content.",
                priority="low",
                impact="Better content discovery and SEO",
                effort="Medium - 1 hour",
                resources=["https://developers.google.com/search/docs/crawling-indexing/links-crawlable"]
            ))
        
<<<<<<< HEAD
        priority_order = {"high": 0, "medium": 1, "low": 2}
        recommendations.sort(key=lambda x: priority_order.get(x.priority, 3))
        
        return recommendations[:8]
=======
        # Sort by priority and return top recommendations
        priority_order = {"high": 0, "medium": 1, "low": 2}
        recommendations.sort(key=lambda x: priority_order.get(x.priority, 3))
        
        return recommendations[:8]  # Return top 8 recommendations
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
    
    def _generate_explanation(self, score: int, features: Dict) -> str:
        """Generate explanation based on score and features"""
        if score >= 90:
            return "Excellent crawlability with strong SEO fundamentals, good performance, and proper technical implementation."
        elif score >= 80:
            return "Good crawlability with solid foundation. Minor optimizations could improve search engine accessibility."
        elif score >= 70:
            return "Fair crawlability with room for improvement in content quality, technical SEO, or performance."
        elif score >= 60:
            return "Poor crawlability with significant issues affecting search engine access. Multiple improvements needed."
        else:
            return "Critical crawlability issues detected. Major improvements required for proper search engine indexing."
    
<<<<<<< HEAD
    def _create_failed_result(self, url: str, error: str) -> ModuleResult:
        """Create result for failed analysis"""
        return ModuleResult(
=======
    def _create_failed_result(self, url: str, error: str) -> NormalizedModuleResult:
        """Create result for failed analysis"""
        return NormalizedModuleResult(
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
            name="Crawlability (Normalized)",
            score=0,
            description="Crawlability analysis failed",
            explanation=f"Unable to analyze crawlability: {error}",
            recommendations=[Recommendation(
                category="Error",
                title="Analysis Failed",
                description=f"Could not analyze website: {error}",
                priority="high",
                impact="Unable to provide recommendations",
                effort="N/A",
                resources=[]
            )],
            confidence=0.0
        )
