from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.staff_request import UpdateStaffRequestSerializer
from ..serializers.staff_response import StaffResponseSerializer
from ..dependencies import services
from ...application.commands.update_staff import UpdateStaffCommand
from ...application.queries.get_staff import GetStaffQuery
class StaffDetailView(APIView):
    def get(self,request,staff_id): return Response(StaffResponseSerializer(services()['staff'].get(GetStaffQuery(staff_id))).data)
    def put(self,request,staff_id):
        s=UpdateStaffRequestSerializer(data=request.data);s.is_valid(raise_exception=True);r=services()['staff'].update(UpdateStaffCommand(staff_id,**s.validated_data));return Response(StaffResponseSerializer(r).data)
