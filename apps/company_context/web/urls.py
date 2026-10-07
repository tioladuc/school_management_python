from django.urls import path

from apps.company_context.web import views
from apps.company_context.web.utilities.url_route_name import UrlRouteName
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
        UrlRouteName.ERROR_PAGE,
        CompanyErrorView.as_view(),
        name=UrlRouteName.ERROR_NAME,
    ),
    path(
        UrlRouteName.COMPANY_ENTRY_PAGE,
        CompanyEntryView.as_view(),
        name=UrlRouteName.COMPANY_ENTRY_NAME,
    ),
    path(
        UrlRouteName.LOGIN_PAGE,
        CompanyLoginView.as_view(),
        name=UrlRouteName.LOGIN_NAME,
    ),
    path(
        UrlRouteName.PASSWORD_RESET_PAGE,
        CompanyPasswordResetView.as_view(),
        name=UrlRouteName.PASSWORD_RESET_NAME,
    ),
    path(
        UrlRouteName.CREATE_ACCOUNT_PAGE,
        CompanyCreateAccountView.as_view(),
        name=UrlRouteName.CREATE_ACCOUNT_NAME,
    ),
    path(
        UrlRouteName.COMPANIES_LIST_PAGE,
        CompanyListView.as_view(),
        name=UrlRouteName.COMPANIES_LIST_NAME,
    ),
    path(
        UrlRouteName.COMPANY_CREATE_PAGE,
        CompanyCreateView.as_view(),
        name=UrlRouteName.COMPANY_CREATE_NAME,
    ),
    path(
        UrlRouteName.COMPANY_UPDATE_PAGE,
        CompanyUpdateView.as_view(),
        name=UrlRouteName.COMPANY_UPDATE_NAME,
    ),
    path(
        UrlRouteName.COMPANY_DELETE_PAGE,
        CompanyDeleteView.as_view(),
        name=UrlRouteName.COMPANY_DELETE_NAME,
    ),
]
