from rest_framework.views import APIView
from rest_framework.response import Response
from ..dependencies import services
from ..serializers.company_request import UpdateCompanyRequestSerializer
from ..serializers.company_response import CompanyResponseSerializer
from ...application.commands.update_company import UpdateCompanyCommand
from ...application.commands.activate_company import ActivateCompanyCommand
from ...application.commands.suspend_company import SuspendCompanyCommand
from ...application.queries.get_company import GetCompanyQuery

class CompanyDetailView(APIView):
    def get(self,request,company_id): return Response(CompanyResponseSerializer(services()['company'].get(GetCompanyQuery(company_id))).data)
    def put(self,request,company_id):
        s=UpdateCompanyRequestSerializer(data=request.data);s.is_valid(raise_exception=True)
        r=services()['company'].update(UpdateCompanyCommand(company_id,**s.validated_data));return Response(CompanyResponseSerializer(r).data)
class CompanyActivateView(APIView):
    def post(self,request,company_id): return Response(CompanyResponseSerializer(services()['company'].activate(ActivateCompanyCommand(company_id))).data)
class CompanySuspendView(APIView):
    def post(self,request,company_id): return Response(CompanyResponseSerializer(services()['company'].suspend(SuspendCompanyCommand(company_id))).data)
