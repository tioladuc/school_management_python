from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.contract_request import UpdateContractRequestSerializer
from ..serializers.contract_response import ContractResponseSerializer
from ..dependencies import services
from ...application.commands.update_contract import UpdateContractCommand
from ...application.commands.activate_contract import ActivateContractCommand
from ...application.commands.suspend_contract import SuspendContractCommand
from ...application.commands.renew_contract import RenewContractCommand
from ...application.queries.get_contract import GetContractQuery
from ...application.queries.get_active_contract import GetActiveContractQuery
class ContractDetailView(APIView):
    def get(self,request,contract_id): return Response(ContractResponseSerializer(services()['contract'].get(GetContractQuery(contract_id))).data)
    def put(self,request,contract_id):
        s=UpdateContractRequestSerializer(data=request.data);s.is_valid(raise_exception=True);r=services()['contract'].update(UpdateContractCommand(contract_id,**s.validated_data));return Response(ContractResponseSerializer(r).data)
class ContractActivateView(APIView):
    def post(self,request,contract_id): return Response(ContractResponseSerializer(services()['contract'].activate(ActivateContractCommand(contract_id))).data)
class ContractSuspendView(APIView):
    def post(self,request,contract_id): return Response(ContractResponseSerializer(services()['contract'].suspend(SuspendContractCommand(contract_id))).data)
class ContractRenewView(APIView):
    def post(self,request,contract_id):
        r=services()['contract'].renew(RenewContractCommand(contract_id, __import__('datetime').date.fromisoformat(request.data['new_end_date'])));return Response(ContractResponseSerializer(r).data)
class ActiveContractView(APIView):
    def get(self,request,company_id):
        r=services()['contract'].active(GetActiveContractQuery(company_id));return Response(ContractResponseSerializer(r).data if r else None)
