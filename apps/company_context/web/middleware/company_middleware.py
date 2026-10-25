from django.shortcuts import redirect

from apps.company_context.infrastructure.orm.company_model import CompanyModel
from apps.company_context.web.utilities.url_route_name import UrlRouteName

# from apps.company_context.infrastructure.repositories.company_repository import CompanyRepository

 

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

        # Authenticated user
        if request.session["logged-in"]: #request.user.is_authenticated:
            return self.get_response(request)

        # Company already stored in session
        company_code = request.session.get("company_code")
        
        if company_code:
            return redirect(UrlRouteName.LOGIN_NAME)
        
        # Company code sent in the request
        company_code = request.POST.get("company_code")
        
        if company_code:
            company = CompanyModel.objects.filter(
                code=company_code
            ).first()

            if company:
                request.session["company_code"] = company_code
                return redirect(UrlRouteName.LOGIN_NAME)

        # Nothing found
        return redirect(UrlRouteName.ERROR_NAME)

    def check_company_existence(self, request): 
        company_code = request.POST.get("company_code")
        if company_code is None:
            company_code = request.session.get("company_code")
        
        # print('GOGOGOG 05 = ', company_code)
        # print(CompanyModel.objects.all())
        # print(CompanyModel.objects.filter(code=company_code).first())
        # print(CompanyRepository.search())
        if company_code:
            self.company = CompanyModel.objects.filter(
                    code=company_code
            ).first()
            return True
        
        else:
            self.company = None
            return False