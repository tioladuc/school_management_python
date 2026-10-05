from django.shortcuts import redirect

from apps.company_context.infrastructure.orm.company_model import CompanyModel

 

class CompanyMiddleware:

    EXCLUDED_PATHS = [
        "/login/",
        "/error-page/",
        "/admin/",
        "/password-reset/",
        "/create-account/",
    ]


    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request): 
        
        # Skip protected checks for specific URLs
        print('duclair')
        if request.path.startswith(tuple(self.EXCLUDED_PATHS)):
            return self.get_response(request)

        print('duclair 01')
        # Authenticated user
        if request.user.is_authenticated:
            return self.get_response(request)

        print('duclair 02')
        # Company already stored in session
        company_code = request.session.get("company_code")

        print('duclair 03')
        if company_code:
            return redirect("login")

        print('duclair 04')
        # Company code sent in the request
        company_code = request.POST.get("company_code")

        print('duclair 05 = ' + company_code)
        if company_code:
            company = CompanyModel.objects.filter(
                code=company_code
            ).first()

            print('duclair 05.1 = ' + str(company))
            print(company)
            if company:
                request.session["company_code"] = company_code
                return redirect("login")

 
        print('duclair 06')
        # Nothing found
        return redirect("error-page")