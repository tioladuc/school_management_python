from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.staff_request import CreateStaffRequestSerializer
from ..serializers.staff_response import StaffResponseSerializer
from ..dependencies import services
from ...application.commands.create_staff import CreateStaffCommand
class StaffCreateView(APIView):
    def post(self,request):
        s=CreateStaffRequestSerializer(data=request.data);s.is_valid(raise_exception=True);r=services()['staff'].create(CreateStaffCommand(**s.validated_data));return Response(StaffResponseSerializer(r).data,status=status.HTTP_201_CREATED)
