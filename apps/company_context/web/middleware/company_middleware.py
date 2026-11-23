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
        self.get_response = get_response


    def __call__(self, request): 
        company_exists = self.check_company_existence(request)
        print("===============TIOTSOP 01===============", request.path)
        # As we login from an outside website
        if request.path == "/":
            print("===============TIOTSOP 02===============", request.path)
            if company_exists:
                print("===============TIOTSOP 03===============", request.path)
                return redirect(UrlRouteName.LOGIN_NAME)
            else:
                print("===============TIOTSOP 04===============", request.path)
                return redirect(UrlRouteName.ERROR_NAME)
        print("===============TIOTSOP 05===============", request.path)
        if request.path.startswith(tuple(self.EXCLUDED_PATHS_MUST_HAVE_COMPANY)) and not company_exists:
            print("===============TIOTSOP 06===============", request.path)
            return redirect(UrlRouteName.ERROR_NAME)
        
        # Skip protected checks for specific URLs
        print("===============TIOTSOP 07===============", request.path)
        if request.path.startswith(tuple(self.EXCLUDED_PATHS)):
            print("===============TIOTSOP 08===============", request.path)
            return self.get_response(request)

        # Authenticated user
        print("===============TIOTSOP 09===============", request.path)
        if request.session["logged-in"]: #request.user.is_authenticated:
            print("===============TIOTSOP 10===============", request.path)
            return self.get_response(request)

        # Company already stored in session
        print("===============TIOTSOP 11===============", request.path)
        company_code = request.session.get("company_code")
        print("===============TIOTSOP 12===============", request.path)
        
        if company_code:
            print("===============TIOTSOP 13===============", request.path)
            return redirect(UrlRouteName.LOGIN_NAME)
        
        # Company code sent in the request
        print("===============TIOTSOP 14===============", request.path)
        company_code = request.POST.get("company_code")
        print("===============TIOTSOP 15===============", request.path)
        if company_code:
            print("===============TIOTSOP 16===============", request.path)
            company = CompanyModel.objects.filter(
                code=company_code
            ).first()
            print("===============TIOTSOP 17===============", request.path)
            if company:
                print("===============TIOTSOP 18===============", request.path)
                request.session["company_code"] = company_code
                return redirect(UrlRouteName.LOGIN_NAME)

        # Nothing found
        print("===============TIOTSOP 19===============", request.path)
        return redirect(UrlRouteName.ERROR_NAME)

    def check_company_existence(self, request): 
        company_code = request.POST.get("company_code")
        if company_code is None:
            company_code = request.session.get("company_code")
        
        if company_code:
            self.company = CompanyModel.objects.filter(
                    code=company_code
            ).first()
            return True
        
        else:
            self.company = None
            return False