from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.company_context.application.queries.search_company import SearchCompanyQuery

from ..forms.company_form import CompanyForm
from ..company_service import get_company_service


class CompanyListView(View):

    template_name = "company_context/companies/company_list.html"

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

    template_name = "company_context/companies/company_form.html"

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

            return redirect("company-list")

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

    template_name = "company_context/companies/company_form.html"

    def get(self, request, company_id):

        service = get_company_service()

        company = service.get_company(company_id)

        if company is None:
            return redirect("company-list")

        form = CompanyForm(
            initial={
                "code": company.code,
                "name": company.name,
                "email": company.email,
                "phone": company.phone,
                "address": company.address,
                "status": company.status,
                "tenant_database": company.tenant_database,
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

            return redirect("company-list")

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

    template_name = (
        "company_context/companies/company_confirm_delete.html"
    )

    def get(self, request, company_id):

        service = get_company_service()

        company = service.get_company(company_id)

        if company is None:
            return redirect("company-list")

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

        return redirect("company-list")