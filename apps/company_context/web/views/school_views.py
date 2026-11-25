from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.company_context.application.commands.create_school import CreateSchoolCommand
from apps.company_context.application.commands.update_school import UpdateSchoolCommand
from apps.company_context.application.dto.school_dto import SchoolDto
from apps.company_context.application.queries.get_school import GetSchoolQuery
from apps.company_context.domain.entities.school import School

from ..forms.school_form import SchoolForm
from ..company_service import get_school_service
from apps.company_context.web.utilities.url_route_name import UrlRouteName


class SchoolListView(View):

    template_name = "school_context/school_list.html"

    def get(self, request):
        db_alias = request.session.get("alias")
        schools = get_school_service().get_all(SchoolDto, db_alias)
        return render(
            request,
            self.template_name,
            {
                "schools": schools,
                "go_academic_year": "/exa/year/",
            },
        )
    
    def post(self, request):
            db_alias = request.session.get("alias")            
            request.session["school_id"] = request.POST['school_id']
            schools = get_school_service().get_all(SchoolDto, db_alias)
            return render(
                request,
                self.template_name,
                {
                    "schools": schools,
                    "go_academic_year": "/exa/year/",
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

        try:
            
            school_dto = getDtoFromForm(form)
            db_alias = request.session.get("alias")

            get_school_service().save(SchoolDto, school_dto, db_alias)
            messages.success(
                request,
                "School created successfully.",
            )

            return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

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
        db_alias = request.session.get("alias")
        school = get_school_service().get_by_id(SchoolDto, school_id, db_alias)

        if school is None:
            return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

        form = getFormFromDto(school) 

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
        db_alias = request.session.get("alias")
        
        try:
            
            school_dto = getDtoFromForm(form, school_id)
            get_school_service().save(SchoolDto, school_dto, db_alias)
            
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

        db_alias = request.session.get("alias")
        school = get_school_service().get_by_id(SchoolDto, school_id, db_alias)

        if school is None:
            return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

        return render(
            request,
            self.template_name,
            {
                "school": school,
            },
        )

    def post(self, request, school_id):

        try:
            db_alias = request.session.get("alias")
            get_school_service().delete(SchoolDto, school_id, db_alias)

            messages.success(
                request,
                "School deleted successfully.",
            )

        except Exception as exc:
            messages.error(
                request,
                str(exc),
            )

        return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

def getDtoFromForm(form, id=None):
    return SchoolDto(
        id=id,
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

def getFormFromDto(dto):
    return SchoolForm(
        initial={
            "code": dto.code,
            "name_fr": dto.name_fr,
            "name_en": dto.name_en,
            "phone": dto.phone,
            "email": dto.email,
            "address": dto.address,
            "autorization": dto.autorization,
            "founder": dto.founder,
            "principal": dto.principal,                
            "city": dto.city,
            "country": dto.country,
            "status": dto.status,
        }
    )