from django.shortcuts import redirect
from apps.company_context.web.utilities.authorization import Authorization
from apps.company_context.web.utilities.url_route_name import UrlRouteName


class UrlAuthorizationMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Company already stored in session
        company_code = request.session.get("company_code")
        
        if company_code:
            return redirect(UrlRouteName.LOGIN_NAME)

        authorization = Authorization()
        if not authorization.urlAuthorization(request):
            return redirect(UrlRouteName.ERROR_NAME)