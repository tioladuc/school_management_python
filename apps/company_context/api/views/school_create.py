from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.school_request import CreateSchoolRequestSerializer
from ..serializers.school_response import SchoolResponseSerializer
from ..dependencies import services
from ...application.commands.create_school import CreateSchoolCommand
class SchoolCreateView(APIView):
    def post(self,request):
        s=CreateSchoolRequestSerializer(data=request.data);s.is_valid(raise_exception=True)
        r=services()['school'].create(CreateSchoolCommand(**s.validated_data));return Response(SchoolResponseSerializer(r).data,status=status.HTTP_201_CREATED)
