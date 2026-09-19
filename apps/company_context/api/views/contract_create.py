from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.contract_request import CreateContractRequestSerializer
from ..serializers.contract_response import ContractResponseSerializer
from ..dependencies import services
from ...application.commands.create_contract import CreateContractCommand
class ContractCreateView(APIView):
    def post(self,request):
        s=CreateContractRequestSerializer(data=request.data);s.is_valid(raise_exception=True)
        r=services()['contract'].create(CreateContractCommand(**s.validated_data));return Response(ContractResponseSerializer(r).data,status=status.HTTP_201_CREATED)
