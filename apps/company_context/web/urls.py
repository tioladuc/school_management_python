from django.urls import path
from .views.company_views import (
    CompanyListView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
)

urlpatterns = [
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
