import time
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.conf import settings

class RateLimitMiddleware:
    """
    Very simple Rate Limiting Middleware using Django Cache.
    Default: 100 requests per minute per IP.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        ip = self.get_client_ip(request)
        key = f"ratelimit_{ip}"
        
        request_count = cache.get(key, 0)
        
        if request_count >= 100:
            return HttpResponseForbidden("Too many requests. Please slow down.")
            
        cache.set(key, request_count + 1, 60) # Block for 1 minute
        
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
