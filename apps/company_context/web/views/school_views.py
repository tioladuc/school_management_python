from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.company_context.application.commands.create_school import CreateSchoolCommand
from apps.company_context.application.commands.update_school import UpdateSchoolCommand
from apps.company_context.application.dto.school_dto import SchoolDto
from apps.company_context.application.queries.get_school import GetSchoolQuery

from ..forms.school_form import SchoolForm
from ..company_service import get_school_service
from apps.company_context.web.utilities.url_route_name import UrlRouteName


class SchoolListView(View):

    template_name = "school_context/school_list.html"

    def get(self, request):
        #print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', request.tenant_db)
        service = get_school_service(request.tenant_db)
        db_alias = request.tenant_db
        schools = service.get_all(db_alias)

        return render(
            request,
            self.template_name,
            {
                "schools": schools,
            },
        )

class SchoolCreateView(View):

    template_name = "school_context/school_form.html"

    def get(self, request):
        form = SchoolForm()

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Create School",
            },
        )

    def post(self, request):
        form = SchoolForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Create School",
                },
            )

        service = get_school_service()

        try:
            service.create(CreateSchoolCommand(
                code=form.cleaned_data["code"],
                name_fr=form.cleaned_data["name_fr"],
                name_en=form.cleaned_data["name_en"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                autorization=form.cleaned_data["autorization"],
                founder=form.cleaned_data["founder"],
                principal=form.cleaned_data["principal"],                
                city=form.cleaned_data["city"],
                country=form.cleaned_data["country"],
                status=form.cleaned_data["status"],)
            )

            messages.success(
                request,
                "School created successfully.",
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

class SchoolUpdateView(View):

    template_name = "school_context/school_form.html"

    def get(self, request, school_id):

        service = get_school_service()
        
        school = service.get(GetSchoolQuery(school_id=school_id))

        if school is None:
            return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

        form = SchoolForm(
            initial={
                "code": school.code,
                "name_fr": school.name_fr,
                "name_en": school.name_en,
                
                "phone": school.phone,
                "email": school.email,
                "address": school.address,

                "autorization": school.autorization,
                "founder": school.founder,
                "principal": school.principal,
                "city": school.city,
                "country": school.country,

                "status": school.status,
            }
        )

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Update School",
                "school": school,
            },
        )

    def post(self, request, school_id):

        form = SchoolForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Update School",
                },
            )

        service = get_school_service()

        try:
            
            service.update(UpdateSchoolCommand(
                id=school_id,
                code=form.cleaned_data["code"],
                name_fr=form.cleaned_data["name_fr"],
                name_en=form.cleaned_data["name_en"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                autorization=form.cleaned_data["autorization"],
                founder=form.cleaned_data["founder"],
                principal=form.cleaned_data["principal"],                
                city=form.cleaned_data["city"],
                country=form.cleaned_data["country"],
                status=form.cleaned_data["status"],)
            )

            messages.success(
                request,
                "School updated successfully.",
            )

            return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

        except Exception as exc:
            form.add_error(None, str(exc))

            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Update School",
                },
            )

class SchoolDeleteView(View):

    template_name = "school_context/school_confirm_delete.html"

    def get(self, request, school_id):

        service = get_school_service()
        ##### service.initialize_company_bd_with_empty_basic_tables(company_id)
        
        # print('before company creation bd+++')
        # service.create_school_from_scratch(company_id)
        # print('after company creation bd++++')

        school = service.get(GetSchoolQuery(school_id=school_id))

        if school is None:
            return redirect(UrlRouteName.COMPANIES_LIST_NAME)

        return render(
            request,
            self.template_name,
            {
                "school": school,
            },
        )

    def post(self, request, school_id):

        service = get_school_service()

        try:
            service.delete_school(school_id)

            messages.success(
                request,
                "School deleted successfully.",
            )

        except Exception as exc:
            messages.error(
                request,
                str(exc),
            )

        return redirect(UrlRouteName.COMPANIES_LIST_NAME)
