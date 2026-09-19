from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.company_request import CreateCompanyRequestSerializer
from ..serializers.company_response import CompanyResponseSerializer
from ..dependencies import services
from ...application.commands.create_company import CreateCompanyCommand

class CompanyCreateView(APIView):
    def post(self, request):
        serializer=CreateCompanyRequestSerializer(data=request.data);serializer.is_valid(raise_exception=True)
        result=services()['company'].create(CreateCompanyCommand(**serializer.validated_data))
        return Response(CompanyResponseSerializer(result).data,status=status.HTTP_201_CREATED)
