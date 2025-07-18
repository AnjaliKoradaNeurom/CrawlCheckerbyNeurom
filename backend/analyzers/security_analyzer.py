import aiohttp
import ssl
import socket
<<<<<<< HEAD
import asyncio # Import asyncio for to_thread and wait_for
from urllib.parse import urlparse
from typing import List, Dict
from models.schemas import Recommendation, ModuleResult
from core.validation import is_google_searchable
=======
from urllib.parse import urlparse
from typing import List, Dict
from pydantic import BaseModel

class Recommendation(BaseModel):
    priority: str
    title: str
    message: str
    code_snippet: str = None
    doc_link: str = None

class ModuleResult(BaseModel):
    name: str
    score: int
    description: str
    explanation: str
    recommendations: List[Recommendation]
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b

class SecurityAnalyzer:
    def __init__(self):
        self.timeout = aiohttp.ClientTimeout(total=30)
    
    async def analyze(self, url: str) -> ModuleResult:
<<<<<<< HEAD
        if not await is_google_searchable(url):
            return ModuleResult(
                name="Security",
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

=======
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        try:
            security_data = await self._analyze_security(url)
            score = self._calculate_security_score(security_data)
            recommendations = self._generate_recommendations(security_data)
            
            return ModuleResult(
                name="Security",
                score=score,
                description="HTTPS and security implementation",
                explanation=self._generate_explanation(score, security_data),
                recommendations=recommendations
            )
        
        except Exception as e:
            return ModuleResult(
                name="Security",
                score=0,
                description="Security analysis failed",
                explanation=f"Unable to analyze security: {str(e)}",
                recommendations=[Recommendation(
                    priority="High",
                    title="Security Analysis Failed",
                    message="Could not analyze security headers and HTTPS configuration.",
                    doc_link="https://developers.google.com/web/fundamentals/security"
                )]
            )
<<<<<<< HEAD
  
    async def _analyze_security(self, url: str) -> Dict:
        parsed_url = urlparse(url)
        
        https_enabled = parsed_url.scheme == 'https'
        
        headers_data = await self._check_security_headers(url)
        
        # Pass the hostname and port to the async SSL check
=======
    
    async def _analyze_security(self, url: str) -> Dict:
        parsed_url = urlparse(url)
        
        # Check HTTPS
        https_enabled = parsed_url.scheme == 'https'
        
        # Get security headers
        headers_data = await self._check_security_headers(url)
        
        # Check SSL certificate
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        ssl_data = await self._check_ssl_certificate(parsed_url.hostname, parsed_url.port or (443 if https_enabled else 80))
        
        return {
            'https': https_enabled,
            'headers': headers_data,
            'ssl': ssl_data,
            'url_scheme': parsed_url.scheme
        }
<<<<<<< HEAD
  
    async def _check_security_headers(self, url: str) -> Dict:
        security_headers = {
            'strict-transport-security': False, 'content-security-policy': False,
            'x-frame-options': False, 'x-content-type-options': False,
            'referrer-policy': False, 'permissions-policy': False
=======
    
    async def _check_security_headers(self, url: str) -> Dict:
        security_headers = {
            'strict-transport-security': False,
            'content-security-policy': False,
            'x-frame-options': False,
            'x-content-type-options': False,
            'referrer-policy': False,
            'permissions-policy': False
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        }
        
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; NeuromBot/1.0)'}) as response:
                    headers = response.headers
<<<<<<< HEAD
                    for header in security_headers.keys():
                        security_headers[header] = header in headers or header.replace('-', '_') in headers
=======
                    
                    for header in security_headers.keys():
                        security_headers[header] = header in headers or header.replace('-', '_') in headers
                    
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
                    return {
                        'headers': security_headers,
                        'headers_present': sum(security_headers.values()),
                        'total_headers': len(security_headers)
                    }
<<<<<<< HEAD
        except Exception:
            return {
                'headers': security_headers, 'headers_present': 0, 'total_headers': len(security_headers)
            }
  
    async def _check_ssl_certificate(self, hostname: str, port: int) -> Dict:
        """
        Checks SSL certificate asynchronously by running synchronous socket/ssl operations in a thread pool.
        """
        if not hostname:
            return {'valid': False, 'error': 'No hostname'}
        
        def _sync_ssl_check():
            # This function will run in a separate thread
            context = ssl.create_default_context()
            # Use a shorter timeout for the socket connection itself
            with socket.create_connection((hostname, port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    return ssock.getpeercert()

        try:
            # Run the synchronous SSL check in a separate thread with an overall timeout
            cert = await asyncio.wait_for(asyncio.to_thread(_sync_ssl_check), timeout=10) # Overall 10s timeout
            
            return {
                'valid': True,
                'subject': dict(x[0] for x in cert.get('subject', [])),
                'issuer': dict(x[0] for x in cert.get('issuer', [])),
                'version': cert.get('version'),
                'not_after': cert.get('notAfter'),
                'not_before': cert.get('notBefore')
            }
        except asyncio.TimeoutError:
            return {'valid': False, 'error': 'SSL certificate check timed out'}
        except Exception as e:
            return {'valid': False, 'error': str(e)}
  
    def _calculate_security_score(self, data: Dict) -> int:
        score = 0
        if data['https']: score += 40
        if data['ssl'].get('valid', False): score += 20
        headers_data = data['headers']
        headers_score = (headers_data['headers_present'] / headers_data['total_headers']) * 40
        score += int(headers_score)
        return min(score, 100)
  
    def _generate_explanation(self, score: int, data: Dict) -> str:
        if score >= 90: return "Excellent security implementation with HTTPS, valid SSL certificate, and comprehensive security headers."
        elif score >= 70: return "Good security foundation with HTTPS enabled, but some security headers could be improved."
        elif score >= 40: return "Basic security with HTTPS, but missing important security headers and configurations."
        else: return "Poor security implementation. HTTPS and security headers need immediate attention."
  
    def _generate_recommendations(self, data: Dict) -> List[Recommendation]:
        recommendations = []
        if not data['https']:
            recommendations.append(Recommendation(
                priority="High", title="Enable HTTPS", message="Secure your website with SSL/TLS encryption for all pages.",
                doc_link="https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https"
            ))
        if not data['ssl'].get('valid', False):
            recommendations.append(Recommendation(
                priority="High", title="Fix SSL Certificate", message="Ensure your SSL certificate is valid and properly configured.",
                doc_link="https://developers.google.com/web/fundamentals/security/encrypt-in-transit/enable-https"
            ))
        headers = data['headers']['headers']
        if not headers.get('strict-transport-security', False):
            recommendations.append(Recommendation(
                priority="High", title="Add HSTS Header", message="Implement HTTP Strict Transport Security to prevent protocol downgrade attacks.",
                code_snippet="Strict-Transport-Security: max-age=31536000; includeSubDomains",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security"
            ))
        if not headers.get('content-security-policy', False):
            recommendations.append(Recommendation(
                priority="Medium", title="Add Content Security Policy", message="Implement CSP to prevent XSS attacks and other code injection vulnerabilities.",
                code_snippet="Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP"
            ))
        if not headers.get('x-frame-options', False):
            recommendations.append(Recommendation(
                priority="Medium", title="Add X-Frame-Options Header", message="Prevent clickjacking attacks by controlling iframe embedding.",
                code_snippet="X-Frame-Options: DENY",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options"
            ))
        if not headers.get('x-content-type-options', False):
            recommendations.append(Recommendation(
                priority="Low", title="Add X-Content-Type-Options Header", message="Prevent MIME type sniffing vulnerabilities.",
                code_snippet="X-Content-Type-Options: nosniff",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options"
            ))
=======
        
        except Exception:
            return {
                'headers': security_headers,
                'headers_present': 0,
                'total_headers': len(security_headers)
            }
    
    async def _check_ssl_certificate(self, hostname: str, port: int) -> Dict:
        if not hostname:
            return {'valid': False, 'error': 'No hostname'}
        
        try:
            # Create SSL context
            context = ssl.create_default_context()
            
            # Connect and get certificate info
            with socket.create_connection((hostname, port), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    
                    return {
                        'valid': True,
                        'subject': dict(x[0] for x in cert.get('subject', [])),
                        'issuer': dict(x[0] for x in cert.get('issuer', [])),
                        'version': cert.get('version'),
                        'not_after': cert.get('notAfter'),
                        'not_before': cert.get('notBefore')
                    }
        
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def _calculate_security_score(self, data: Dict) -> int:
        score = 0
        
        # HTTPS (40 points)
        if data['https']:
            score += 40
        
        # SSL Certificate (20 points)
        if data['ssl'].get('valid', False):
            score += 20
        
        # Security Headers (40 points total)
        headers_data = data['headers']
        headers_score = (headers_data['headers_present'] / headers_data['total_headers']) * 40
        score += int(headers_score)
        
        return min(score, 100)
    
    def _generate_explanation(self, score: int, data: Dict) -> str:
        if score >= 90:
            return "Excellent security implementation with HTTPS, valid SSL certificate, and comprehensive security headers."
        elif score >= 70:
            return "Good security foundation with HTTPS enabled, but some security headers could be improved."
        elif score >= 40:
            return "Basic security with HTTPS, but missing important security headers and configurations."
        else:
            return "Poor security implementation. HTTPS and security headers need immediate attention."
    
    def _generate_recommendations(self, data: Dict) -> List[Recommendation]:
        recommendations = []
        
        # HTTPS recommendations
        if not data['https']:
            recommendations.append(Recommendation(
                priority="High",
                title="Enable HTTPS",
                message="Secure your website with SSL/TLS encryption for all pages.",
                doc_link="https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https"
            ))
        
        # SSL Certificate recommendations
        if not data['ssl'].get('valid', False):
            recommendations.append(Recommendation(
                priority="High",
                title="Fix SSL Certificate",
                message="Ensure your SSL certificate is valid and properly configured.",
                doc_link="https://developers.google.com/web/fundamentals/security/encrypt-in-transit/enable-https"
            ))
        
        # Security Headers recommendations
        headers = data['headers']['headers']
        
        if not headers.get('strict-transport-security', False):
            recommendations.append(Recommendation(
                priority="High",
                title="Add HSTS Header",
                message="Implement HTTP Strict Transport Security to prevent protocol downgrade attacks.",
                code_snippet="Strict-Transport-Security: max-age=31536000; includeSubDomains",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security"
            ))
        
        if not headers.get('content-security-policy', False):
            recommendations.append(Recommendation(
                priority="Medium",
                title="Add Content Security Policy",
                message="Implement CSP to prevent XSS attacks and other code injection vulnerabilities.",
                code_snippet="Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP"
            ))
        
        if not headers.get('x-frame-options', False):
            recommendations.append(Recommendation(
                priority="Medium",
                title="Add X-Frame-Options Header",
                message="Prevent clickjacking attacks by controlling iframe embedding.",
                code_snippet="X-Frame-Options: DENY",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options"
            ))
        
        if not headers.get('x-content-type-options', False):
            recommendations.append(Recommendation(
                priority="Low",
                title="Add X-Content-Type-Options Header",
                message="Prevent MIME type sniffing vulnerabilities.",
                code_snippet="X-Content-Type-Options: nosniff",
                doc_link="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options"
            ))
        
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
        return recommendations
