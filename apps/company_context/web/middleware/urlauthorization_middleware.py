from django.shortcuts import redirect
from apps.company_context.web.utilities.authorization import Authorization
from apps.company_context.web.utilities.url_route_name import UrlRouteName


class UrlAuthorizationMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Company already stored in session
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX 01')
        company_code = request.session.get("company_code")
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX 02')
        if company_code:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXX 0222')
            return redirect(UrlRouteName.LOGIN_NAME)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX 03')
        authorization = Authorization()
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX 04')
        if not authorization.urlAuthorization(request):
            print('XXXXXXXXXXXXXXXXXXXXXXXXXX 04444')
            return redirect(UrlRouteName.ERROR_NAME)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXX 05')