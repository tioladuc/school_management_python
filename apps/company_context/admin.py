from django.contrib import admin
from .infrastructure.orm.models import CompanyModel,SchoolModel,StaffModel,ContractModel,ContractDataModel,SubscriptionModel
admin.site.register([CompanyModel,SchoolModel,StaffModel,ContractModel,ContractDataModel,SubscriptionModel])
