from django.urls import path

from apps.company_context.web import views
from .views.company_views import (
    CompanyErrorView,
    CompanyListView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    CompanyEntryView,
    CompanyLoginView,
    CompanyPasswordResetView,
    CompanyCreateAccountView,
)

urlpatterns = [
    path(
        "error-page/",
        CompanyErrorView.as_view(),
        name="error-page"
        ),
    path(
        "company-entry/",
        CompanyEntryView.as_view(),
        name="company-entry"
    ),
    path(
        "login/",
        CompanyLoginView.as_view(),
        name="login"
        ),
    path(
            "password-reset/",
            CompanyPasswordResetView.as_view(),
            name="password-reset"
            ),
    path(
                "create-account/",
                CompanyCreateAccountView.as_view(),
                name="create-account"
                ),
    path(
        "companies/",
        CompanyListView.as_view(),
        name="company-list",
    ),

    path(
        "companies/create/",
        CompanyCreateView.as_view(),
        name="company-create",
    ),

    path(
        "companies/<int:company_id>/edit/",
        CompanyUpdateView.as_view(),
        name="company-update",
    ),

    path(
        "companies/<int:company_id>/delete/",
        CompanyDeleteView.as_view(),
        name="company-delete",
    ),
]
