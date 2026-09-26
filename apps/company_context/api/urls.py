from django.urls import path
from .views.company_create import CompanyCreateView
from .views.company import CompanyDetailView, CompanyActivateView, CompanyListView, CompanySuspendView
from .views.school_create import SchoolCreateView
from .views.school import SchoolDetailView, CompanySchoolListView
from .views.contract_create import ContractCreateView
from .views.contract import (
    ContractDetailView,
    ContractActivateView,
    ContractSuspendView,
    ContractRenewView,
    ActiveContractView,
)
from .views.staff_create import StaffCreateView
from .views.staff import StaffDetailView
from .views.billing import CompanyBillingHistoryView

urlpatterns = [
    path("companies", CompanyCreateView.as_view()),
    path("companies/all", CompanyListView.as_view()),
    path("companies/<int:company_id>", CompanyDetailView.as_view()),
    path("companies/<int:company_id>/activate", CompanyActivateView.as_view()),
    path("companies/<int:company_id>/suspend", CompanySuspendView.as_view()),
    path("companies/<int:company_id>/schools", CompanySchoolListView.as_view()),
    path("schools", SchoolCreateView.as_view()),
    path("schools/<int:school_id>", SchoolDetailView.as_view()),
    path("contracts", ContractCreateView.as_view()),
    path("contracts/<int:contract_id>", ContractDetailView.as_view()),
    path("contracts/<int:contract_id>/activate", ContractActivateView.as_view()),
    path("contracts/<int:contract_id>/suspend", ContractSuspendView.as_view()),
    path("contracts/<int:contract_id>/renew", ContractRenewView.as_view()),
    path("companies/<int:company_id>/contracts/active", ActiveContractView.as_view()),
    path("staff", StaffCreateView.as_view()),
    path("staff/<int:staff_id>", StaffDetailView.as_view()),
    path("companies/<int:company_id>/billing", CompanyBillingHistoryView.as_view()),
]
