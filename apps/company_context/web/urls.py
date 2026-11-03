from django.urls import path

from apps.company_context.web import views
from apps.company_context.web.utilities.url_route_name import UrlRouteName
from apps.company_context.web.views.school_views import SchoolCreateView, SchoolDeleteView, SchoolListView, SchoolUpdateView
from .views.company_views import (
    CompanyErrorView,
    
    CompanyListView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,

    CompanyManageBDView,
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
    #  for companies
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
        UrlRouteName.COMPANY_MANAGE_BD_PAGE,
        CompanyManageBDView.as_view(),
        name=UrlRouteName.COMPANY_MANAGE_BD_NAME,
    ),

    path(
            UrlRouteName.COMPANY_DELETE_PAGE,
            CompanyDeleteView.as_view(),
            name=UrlRouteName.COMPANY_DELETE_NAME,
        ),

    #  for schools
        path(
            UrlRouteName.SCHOOLS_LIST_PAGE,
            SchoolListView.as_view(),
            name=UrlRouteName.SCHOOLS_LIST_NAME,
        ),
        path(
            UrlRouteName.SCHOOL_CREATE_PAGE,
            SchoolCreateView.as_view(),
            name=UrlRouteName.SCHOOL_CREATE_NAME,
        ),
        path(
            UrlRouteName.SCHOOL_UPDATE_PAGE,
            SchoolUpdateView.as_view(),
            name=UrlRouteName.SCHOOL_UPDATE_NAME,
        ),
        #path(
        #    UrlRouteName.SCHOOL_MANAGE_BD_PAGE,
        #    SchoolManageBDView.as_view(),
        #    name=UrlRouteName.SCHOOL_MANAGE_BD_NAME,
        #),
    
        path(
                UrlRouteName.SCHOOL_DELETE_PAGE,
                SchoolDeleteView.as_view(),
                name=UrlRouteName.SCHOOL_DELETE_NAME,
            ),
]
