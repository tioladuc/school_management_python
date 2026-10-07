from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.company_context.application.dto.user_in_dto import UserInDto
from apps.company_context.application.queries.search_company import SearchCompanyQuery
from apps.company_context.application.queries.get_company import GetCompanyQuery
from apps.company_context.web.utilities.url_route_name import UrlRouteName

from ..forms.company_form import CompanyForm
from ..company_service import get_company_service

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from apps.company_context.infrastructure.orm.models import CompanyModel
from django.utils.decorators import method_decorator


class CompanyErrorView(View):

    template_name = "company_context/company_error.html"

    def get(self, request):
        print('CompanyErrorView.get()')
        
        return render(
            request,
            self.template_name,
            {},
        )
    def post(self, request):
        print('CompanyErrorView.post()')
        return render(
            request,
            self.template_name,
            {},
        )

class CompanyLoginView(View):

    template_name_login = "company_context/company_login.html"
    template_name_home = "company_context/company_dashboard.html"

    def get(self, request):
        service = get_company_service()
        return render(
            request,
            self.template_name_login,
            {
                "schools": service.getSchools(),
                "profiles": service.getProfiles(),
            },
        )

    def post(self, request):
        # 1. Read data coming from the HTML form
        school_id = request.POST.get("school_id")
        profile = request.POST.get("profile")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 2. Get application service
        service = get_company_service()

        # 3. Send the data to the application layer
        userInDto = UserInDto(
            company_code=request.session.get("company_code"),
            school_id=school_id,
            profile=profile,
            username=username,
            password=password,
        )
        result = service.login(userInDto)

        # 4. Handle the result
        if not result.success:
            return render(
                request,
                self.template_name_login,
                {
                    "schools": service.getSchools(),
                    "profiles": service.getProfiles(),
                    "error": result.message,
                },
            )

        # 5. Login successful
        request.session["school_id"] = school_id
        request.session["profile"] = profile
        request.session["user_data"] = result.user_data

        return redirect(self.template_name_home)


class CompanyPasswordResetView(View):

    template_name = "company_context/company_passwordreset.html"

    def get(self, request):
        service = get_company_service()
        return render(
            request,
            self.template_name,
            {
                "schools": service.getSchools(),
                "profiles": service.getProfiles(),
            },
        )

    def post(self, request):
        service = get_company_service()
        return render(
            request,
            self.template_name,
            {
                "schools": service.getSchools(),
                "profiles": service.getProfiles(),
            },
        )


class CompanyCreateAccountView(View):

    template_name = "company_context/company_newaccount.html"

    def get(self, request):
        service = get_company_service()
        print(service.getProfiles())
        return render(
            request,
            self.template_name,
            {
                "schools": service.getSchools(),
                "profiles": service.getProfiles(),
            },
        )

    def post(self, request):
        service = get_company_service()
        print(request.POST)
        return render(
            request,
            self.template_name,
            {
                "schools": service.getSchools(),
                "profiles": service.getProfiles(),
            },
        )


class CompanyListView(View):

    template_name = "company_context/company_list.html"

    def get(self, request):
        service = get_company_service()

        companies = service.search(SearchCompanyQuery("", None))

        return render(
            request,
            self.template_name,
            {
                "companies": companies,
            },
        )


class CompanyCreateView(View):

    template_name = "company_context/company_form.html"

    def get(self, request):
        form = CompanyForm()

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Create Company",
            },
        )

    def post(self, request):
        form = CompanyForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Create Company",
                },
            )

        service = get_company_service()

        try:
            service.create_company(
                code=form.cleaned_data["code"],
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data["address"],
                status=form.cleaned_data["status"],
                tenant_database=form.cleaned_data["tenant_database"],
            )

            messages.success(
                request,
                "Company created successfully.",
            )

            return redirect(UrlRouteName.COMPANIES_LIST_NAME)

        except Exception as exc:
            form.add_error(None, str(exc))

            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Create Company",
                },
            )


class CompanyUpdateView(View):

    template_name = "company_context/company_form.html"

    def get(self, request, company_id):

        service = get_company_service()
        
        company = service.get(GetCompanyQuery(company_id=company_id))

        if company is None:
            return redirect(UrlRouteName.COMPANIES_LIST_NAME)

        form = CompanyForm(
            initial={
                "code": company.code,
                "name": company.name,
                "email": company.email,
                "phone": company.phone,
                "address": company.address,
                "status": company.status,
                # "tenant_database": company.tenant_database,
            }
        )

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Update Company",
                "company": company,
            },
        )

    def post(self, request, company_id):

        form = CompanyForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Update Company",
                },
            )

        service = get_company_service()

        try:
            service.update_company(
                company_id=company_id,
                code=form.cleaned_data["code"],
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data["address"],
                status=form.cleaned_data["status"],
                tenant_database=form.cleaned_data["tenant_database"],
            )

            messages.success(
                request,
                "Company updated successfully.",
            )

            return redirect(UrlRouteName.COMPANIES_LIST_NAME)

        except Exception as exc:
            form.add_error(None, str(exc))

            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Update Company",
                },
            )


class CompanyDeleteView(View):

    template_name = "company_context/company_confirm_delete.html"

    def get(self, request, company_id):

        service = get_company_service()

        company = service.get_company(company_id)

        if company is None:
            return redirect(UrlRouteName.COMPANIES_LIST_NAME)

        return render(
            request,
            self.template_name,
            {
                "company": company,
            },
        )

    def post(self, request, company_id):

        service = get_company_service()

        try:
            service.delete_company(company_id)

            messages.success(
                request,
                "Company deleted successfully.",
            )

        except Exception as exc:
            messages.error(
                request,
                str(exc),
            )

        return redirect(UrlRouteName.COMPANIES_LIST_NAME)


@method_decorator(csrf_exempt, name="dispatch")
class CompanyEntryView(View):

    def post(self, request):

        company_code = request.POST.get("company_code")

        if not company_code:
            return redirect(UrlRouteName.ERROR_NAME)

        company = CompanyModel.objects.filter(code=company_code).first()

        if not company:
            return redirect(UrlRouteName.ERROR_NAME)

        request.session["company_code"] = company_code

        return redirect(UrlRouteName.LOGIN_NAME)

    def get(self, request):
        return redirect(UrlRouteName.ERROR_NAME)
