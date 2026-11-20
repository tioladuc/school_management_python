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
from ..company_service import get_school_service, get_school_serviceAAA
from apps.company_context.web.utilities.url_route_name import UrlRouteName


class SchoolListView(View):

    template_name = "school_context/school_list.html"

    def get(self, request):
        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', request.session.get("alias"))
        db_alias = request.session.get("alias")
        service = get_school_service(db_alias)
        print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', db_alias)
        #schools = service.get_all(db_alias)
        schools = get_school_serviceAAA().get_all(SchoolDto, db_alias)
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

        service = get_school_service(request.session.get("alias"))

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
        db_alias = request.session.get("alias")
        service = get_school_service(db_alias)        
        school = service.get_by_id(school_id, db_alias)

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
        print('yoyoyoyoyoyoyoyoy')
        form = SchoolForm(request.POST)
        print('yayayayayayayay', form.is_valid())
        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Update School",
                },
            )
        print('yayayayayayayay 111111111', form.is_valid())
        db_alias = request.session.get("alias")
        print('yayayayayayayay 22222222', db_alias)
        service = get_school_service(db_alias)
        print('yayayayayayayay 33333333', form.is_valid())

        try:
            print('yayayayayayayay444444444++++', form.is_valid())
            school_dto = SchoolDto(
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
            print('WEWEWEWEWEWEWEWEWEWEWEW', form.is_valid())
            get_school_serviceAAA().save(SchoolDto, school_dto, db_alias)
            #service.update(school_id, school_dto,
            #    db_alias
            #)
            print('yayayayayayayay5555555555555', form.is_valid())

            """service.update(school_id, UpdateSchoolCommand(
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
                            status=form.cleaned_data["status"],),
                            db_alias
                        )"""
            print('yayayayayayayay777777777777', form.is_valid())
            messages.success(
                request,
                "School updated successfully.",
            )
            print('yayayayayayayay555555555555', form.is_valid())

            return redirect(UrlRouteName.SCHOOLS_LIST_NAME)

        except Exception as exc:
            print('yayayayayayayayDDDDDDDDDDD', form.is_valid())
            form.add_error(None, str(exc))
            print('yayayayayayayayAAAAAAAAAAAAA', form.is_valid())
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

        service = get_school_service(request.session.get("alias"))
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

        service = get_school_service(request.session.get("alias"))

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
