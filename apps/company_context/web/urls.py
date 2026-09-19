from django.urls import path
from .views.company_views import CompanyCreateWebView
from .views.pages import company_created
urlpatterns=[path('companies/new/',CompanyCreateWebView.as_view(),name='company-create'),path('companies/created/',company_created,name='company-created')]
