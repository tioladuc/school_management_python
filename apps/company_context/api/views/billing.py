from rest_framework.views import APIView
from rest_framework.response import Response
from ..dependencies import services
from ..serializers.contract_data_response import ContractDataResponseSerializer
from ...application.queries.get_billing_history import GetBillingHistoryQuery


class CompanyBillingHistoryView(APIView):
    def get(self, request, company_id):
        return Response(
            ContractDataResponseSerializer(
                services()["billing"].history(GetBillingHistoryQuery(company_id)),
                many=True,
            ).data
        )
