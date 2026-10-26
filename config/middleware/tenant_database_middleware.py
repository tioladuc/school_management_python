from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class TenantDatabaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        alias = request.session.get("alias")

        if alias:
            # The alias must already be registered in settings.DATABASES.
            if alias not in settings.DATABASES:
                raise ImproperlyConfigured(
                    f"Unknown database alias: {alias!r}"
                )

            request.tenant_db = alias
        else:
            request.tenant_db = "default"

        # print('DUCLAIR TIOTSOP LAMBOU . . .', request.tenant_db, request.session.get("alias"))
        return self.get_response(request)