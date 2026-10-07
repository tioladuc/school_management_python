from django.shortcuts import redirect

from apps.company_context.infrastructure.orm.company_model import CompanyModel
from apps.company_context.web.utilities.url_route_name import UrlRouteName

 

class CompanyMiddleware:

    EXCLUDED_PATHS = [
        "/" + UrlRouteName.LOGIN_PAGE,
        "/" + UrlRouteName.ERROR_PAGE,
        "/" + UrlRouteName.ADMIN_PAGE,
        "/" + UrlRouteName.PASSWORD_RESET_PAGE,
        "/" + UrlRouteName.CREATE_ACCOUNT_PAGE,
    ]

    EXCLUDED_PATHS_MUST_HAVE_COMPANY = [
            "/" + UrlRouteName.LOGIN_PAGE,
            "/" + UrlRouteName.PASSWORD_RESET_PAGE,
            "/" + UrlRouteName.CREATE_ACCOUNT_PAGE,
        ]

    company = None

    def __init__(self, get_response):
        print('CompanyMiddleware.__init__()')
        self.get_response = get_response


    def __call__(self, request): 
        company_exists = self.check_company_existence(request)
        if request.path.startswith(tuple(self.EXCLUDED_PATHS_MUST_HAVE_COMPANY)) and not company_exists:
            return redirect(UrlRouteName.ERROR_NAME)
        
        # Skip protected checks for specific URLs
        if request.path.startswith(tuple(self.EXCLUDED_PATHS)):
            return self.get_response(request)

        print('duclair 01')
        # Authenticated user
        if True: # request.user.is_authenticated:
            return self.get_response(request)

        print('duclair 02')
        # Company already stored in session
        company_code = request.session.get("company_code")

        print('duclair 03')
        if company_code:
            return redirect(UrlRouteName.LOGIN_NAME)

        print('duclair 04')
        # Company code sent in the request
        company_code = request.POST.get("company_code")

        # print('duclair 05 = ' + company_code)
        if company_code:
            company = CompanyModel.objects.filter(
                code=company_code
            ).first()

            print('duclair 05.1 = ' + str(company))
            print(company)
            if company:
                request.session["company_code"] = company_code
                return redirect(UrlRouteName.LOGIN_NAME)

 
        print('duclair 06')
        # Nothing found
        return redirect(UrlRouteName.ERROR_NAME)

    def check_company_existence(self, request): 
        company_code = request.POST.get("company_code")
        if company_code is None:
            company_code = request.session.get("company_code")
        
        print('GOGOGOG 05 = ')
        print(company_code)
        if company_code:
            self.company = CompanyModel.objects.filter(
                    code=company_code
            ).first()
            return True
        
        else:
            self.company = None
            return False