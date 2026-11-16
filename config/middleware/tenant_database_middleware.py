from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class TenantDatabaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        alias = request.session.get("alias")
       
        if alias:
            # The alias must already be registered in settings.DATABASES.
            if alias not in settings.DATABASES and request.META.get("HTTP_REFERER") and "/companies/" not in request.META.get("HTTP_REFERER"):
                raise ImproperlyConfigured(
                    f"Unknown database alias: {alias!r}"
                )

            request.tenant_db = alias
        else:
            request.tenant_db = "default"
            
        return self.get_response(request)