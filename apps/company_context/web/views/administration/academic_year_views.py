from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse

from apps.company_context.application.dto.academic_year_dto import AcademicYearDto
from apps.company_context.web.forms.administration.academic_year_forms import AcademicYearForm

# Adapt this import to your actual service accessor
from ...company_service import get_school_service


class AcademicYearView(View):

    list_template_name = (
        "school_context/administration/academic_year/list.html"
    )

    form_template_name = (
        "school_context/administration/academic_year/form.html"
    )

    detail_template_name = (
        "school_context/administration/academic_year/detail.html"
    )

    delete_template_name = (
        "school_context/administration/academic_year/delete.html"
    )

    # ---------------------------------------------------------
    # URL helper
    # ---------------------------------------------------------
    myRequest = None

    def get_url(self, action="list", academic_year_id=None):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 01')
        #url = reverse("academic_year_crud")
        url = self.myRequest.path

        params = f"?action={action}"

        if academic_year_id is not None:
            params += f"&id={academic_year_id}"

        return f"{url}{params}"

    # ---------------------------------------------------------
    # Session / context
    # ---------------------------------------------------------

    def get_context_data(self, request):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 02')
        self.myRequest = request
        db_alias = request.session.get("alias")
        school_id = request.session.get("school_id")#DUCLAIRTIOTSOP

        if db_alias is None or school_id is None:
            return None

        try:
            school_id = int(school_id)
        except (TypeError, ValueError):
            return None

        return {
            "db_alias": db_alias,
            "school_id": school_id,
        }

    # ---------------------------------------------------------
    # Retrieve academic year
    # ---------------------------------------------------------

    def get_academic_year(self, academic_year_id, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 03')
        academic_year = (
            get_school_service()
            .get_by_id(AcademicYearDto, academic_year_id, db_alias)
        )

        if academic_year is None:
            return None

        # Multi-school security
        if academic_year.school_id != school_id:
            return None

        return academic_year

    # ---------------------------------------------------------
    # GET
    # ---------------------------------------------------------

    def get(self, request, *args, **kwargs):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 04')
        self.myRequest = request
        action = request.GET.get("action", "list")

        context_data = self.get_context_data(request)

        if context_data is None:
            messages.error(request, "School context is missing.")
            return redirect("/")

        db_alias = context_data["db_alias"]
        school_id = context_data["school_id"]

        if action == "list":
            return self.list(request, db_alias, school_id)

        if action == "create":
            return self.create(request)

        if action == "detail":
            return self.detail(request, db_alias, school_id)

        if action == "update":
            return self.update(request, db_alias, school_id)

        if action == "delete":
            return self.delete(request, db_alias, school_id)

        messages.error(request, "Invalid action.")

        return redirect(self.get_url("list"))

    # ---------------------------------------------------------
    # POST
    # ---------------------------------------------------------

    def post(self, request, *args, **kwargs):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 05')
        self.myRequest = request
        action = request.POST.get("action", "list")

        context_data = self.get_context_data(request)

        if context_data is None:
            messages.error(request, "School context is missing.")
            return redirect("/")

        db_alias = context_data["db_alias"]
        school_id = context_data["school_id"]

        if action == "create":
            return self.create_post(request, db_alias, school_id)

        if action == "update":
            return self.update_post(request, db_alias, school_id)

        if action == "delete":
            return self.delete_post(request, db_alias, school_id)

        messages.error(request, "Invalid action.")

        return redirect(self.get_url("list"))

    # =========================================================
    # LIST / SEARCH / FILTER / PAGINATION
    # =========================================================

    def list(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 06')
        self.myRequest = request
        academic_years = (
            get_school_service()
            .get_all(AcademicYearDto, db_alias)
        )
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 061')
        # Filter by school
        academic_years = [
            academic_year
            for academic_year in academic_years
            if academic_year.school_id == school_id
        ]
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 062')
        # -----------------------------------------------------
        # Search
        # -----------------------------------------------------

        search = request.GET.get("search", "").strip()
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 063')
        if search:
            print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 063')
            academic_years = [
                academic_year
                for academic_year in academic_years
                if search.lower() in str(academic_year.year).lower()
            ]

        # -----------------------------------------------------
        # Filter by status
        # -----------------------------------------------------
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 064')
        status = request.GET.get("status", "").strip()
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 065')
        if status:
            print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 066')
            academic_years = [
                academic_year
                for academic_year in academic_years
                if academic_year.status == status
            ]

        # -----------------------------------------------------
        # Filter by year range
        # -----------------------------------------------------
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 067')
        year_from = request.GET.get("year_from", "").strip()
        year_to = request.GET.get("year_to", "").strip()
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 068')
        if year_from:

            try:
                year_from = int(year_from)

                academic_years = [
                    academic_year
                    for academic_year in academic_years
                    if academic_year.year >= year_from
                ]

            except ValueError:
                year_from = ""
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 069')
        if year_to:

            try:
                year_to = int(year_to)

                academic_years = [
                    academic_year
                    for academic_year in academic_years
                    if academic_year.year <= year_to
                ]

            except ValueError:
                year_to = ""

        # -----------------------------------------------------
        # Sort
        # -----------------------------------------------------
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 0610')
        academic_years = sorted(
            academic_years,
            key=lambda x: x.year,
            reverse=True,
        )

        # -----------------------------------------------------
        # Pagination
        # -----------------------------------------------------

        paginator = Paginator(academic_years, 10)

        page_number = request.GET.get("page")

        page_obj = paginator.get_page(page_number)
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 0611')
        context = {
            "academic_years": page_obj,
            "page_obj": page_obj,
            "search": search,
            "status": status,
            "year_from": year_from,
            "year_to": year_to,
            "total_count": paginator.count,
            "active_count": sum(
                1 for academic_year in academic_years
                if academic_year.status == "ACTIVE"
            ),
            "inactive_count": sum(
                1 for academic_year in academic_years
                if academic_year.status == "INACTIVE"
            ),
            "create_url": self.get_url("create"),
            "crud_url": self.myRequest.path, #self.get_url("list"),

        }
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 0612')
        return render(
            request,
            self.list_template_name,
            context,
        )

    # =========================================================
    # CREATE
    # =========================================================

    def create(self, request):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 07')
        self.myRequest = request
        form = AcademicYearForm()

        return render(
            request,
            self.form_template_name,
            {
                "form": form,
                "title": "Create Academic Year",
                "action": "create",
                "crud_url": self.get_url("list"),
            },
        )

    def create_post(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 08')
        self.myRequest = request
        form = AcademicYearForm(request.POST)

        if not form.is_valid():

            return render(
                request,
                self.form_template_name,
                {
                    "form": form,
                    "title": "Create Academic Year",
                    "action": "create",
                    "crud_url": self.get_url("list"),
                },
            )

        try:

            academic_year_dto = AcademicYearDto(
                school_id=school_id,
                year=form.cleaned_data["year"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                status=form.cleaned_data["status"],
            )

            get_school_service().save(
                AcademicYearDto,
                academic_year_dto,
                db_alias,
            )

            messages.success(
                request,
                "Academic year created successfully.",
            )

            return redirect(self.get_url("list"))

        except Exception as exc:

            form.add_error(None, str(exc))

            return render(
                request,
                self.form_template_name,
                {
                    "form": form,
                    "title": "Create Academic Year",
                    "action": "create",
                    "crud_url": self.get_url("list"),
                },
            )

    # =========================================================
    # DETAIL
    # =========================================================

    def detail(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 09')
        academic_year_id = request.GET.get("id")
        self.myRequest = request

        if not academic_year_id:

            messages.error(request, "Academic year ID is missing.")

            return redirect(self.get_url("list"))

        academic_year = self.get_academic_year(
            academic_year_id,
            db_alias,
            school_id,
        )

        if academic_year is None:

            messages.error(request, "Academic year not found.")

            return redirect(self.get_url("list"))

        return render(
            request,
            self.detail_template_name,
            {
                "academic_year": academic_year,
                "crud_url": self.get_url("list"),
                "update_url": self.get_url(
                    "update",
                    academic_year.id,
                ),
                "delete_url": self.get_url(
                    "delete",
                    academic_year.id,
                ),
            },
        )

    # =========================================================
    # UPDATE
    # =========================================================

    def update(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 10')
        academic_year_id = request.GET.get("id")
        self.myRequest = request

        if not academic_year_id:

            messages.error(request, "Academic year ID is missing.")

            return redirect(self.get_url("list"))

        academic_year = self.get_academic_year(
            academic_year_id,
            db_alias,
            school_id,
        )

        if academic_year is None:

            messages.error(request, "Academic year not found.")

            return redirect(self.get_url("list"))

        form = AcademicYearForm(
            initial={
                "year": academic_year.year,
                "start_date": academic_year.start_date,
                "end_date": academic_year.end_date,
                "status": academic_year.status,
            }
        )

        return render(
            request,
            self.form_template_name,
            {
                "form": form,
                "title": "Update Academic Year",
                "action": "update",
                "academic_year": academic_year,
                "crud_url": self.get_url("list"),
            },
        )

    def update_post(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 11')
        academic_year_id = request.POST.get("id")
        self.myRequest = request

        if not academic_year_id:

            messages.error(request, "Academic year ID is missing.")

            return redirect(self.get_url("list"))

        academic_year = self.get_academic_year(
            academic_year_id,
            db_alias,
            school_id,
        )

        if academic_year is None:

            messages.error(request, "Academic year not found.")

            return redirect(self.get_url("list"))

        form = AcademicYearForm(request.POST)

        if not form.is_valid():

            return render(
                request,
                self.form_template_name,
                {
                    "form": form,
                    "title": "Update Academic Year",
                    "action": "update",
                    "academic_year": academic_year,
                    "crud_url": self.get_url("list"),
                },
            )

        try:

            academic_year_dto = AcademicYearDto(
                id=academic_year.id,
                school_id=school_id,
                year=form.cleaned_data["year"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                status=form.cleaned_data["status"],
                created_at=academic_year.created_at,
                updated_at=academic_year.updated_at,
            )

            get_school_service().save(
                AcademicYearDto,
                academic_year_dto,
                db_alias,
            )

            messages.success(
                request,
                "Academic year updated successfully.",
            )

            return redirect(
                self.get_url(
                    "detail",
                    academic_year.id,
                )
            )

        except Exception as exc:

            form.add_error(None, str(exc))

            return render(
                request,
                self.form_template_name,
                {
                    "form": form,
                    "title": "Update Academic Year",
                    "action": "update",
                    "academic_year": academic_year,
                    "crud_url": self.get_url("list"),
                },
            )

    # =========================================================
    # DELETE
    # =========================================================

    def delete(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 12')
        academic_year_id = request.GET.get("id")
        self.myRequest = request

        if not academic_year_id:

            messages.error(request, "Academic year ID is missing.")

            return redirect(self.get_url("list"))

        academic_year = self.get_academic_year(
            academic_year_id,
            db_alias,
            school_id,
        )

        if academic_year is None:

            messages.error(request, "Academic year not found.")

            return redirect(self.get_url("list"))

        return render(
            request,
            self.delete_template_name,
            {
                "academic_year": academic_year,
                "crud_url": self.get_url("list"),
            },
        )

    def delete_post(self, request, db_alias, school_id):
        print('SSSSSSSSSSSSSSSSSSSS PPPPPPPP 13')
        self.myRequest = request
        academic_year_id = request.POST.get("id")

        if not academic_year_id:

            messages.error(request, "Academic year ID is missing.")

            return redirect(self.get_url("list"))

        academic_year = self.get_academic_year(
            academic_year_id,
            db_alias,
            school_id,
        )

        if academic_year is None:

            messages.error(request, "Academic year not found.")

            return redirect(self.get_url("list"))

        try:

            get_school_service().delete(
                AcademicYearDto,
                academic_year.id,
                db_alias,
            )

            messages.success(
                request,
                "Academic year deleted successfully.",
            )

            return redirect(self.get_url("list"))

        except Exception as exc:

            messages.error(
                request,
                f"Unable to delete academic year: {exc}",
            )

            return redirect(
                self.get_url(
                    "detail",
                    academic_year.id,
                )
            )