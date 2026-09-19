from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.school_request import UpdateSchoolRequestSerializer
from ..serializers.school_response import SchoolResponseSerializer
from ..dependencies import services
from ...application.commands.update_school import UpdateSchoolCommand
from ...application.queries.get_school import GetSchoolQuery
from ...application.queries.list_company_schools import ListCompanySchoolsQuery
class SchoolDetailView(APIView):
    def get(self,request,school_id): return Response(SchoolResponseSerializer(services()['school'].get(GetSchoolQuery(school_id))).data)
    def put(self,request,school_id):
        s=UpdateSchoolRequestSerializer(data=request.data);s.is_valid(raise_exception=True)
        r=services()['school'].update(UpdateSchoolCommand(school_id,**s.validated_data));return Response(SchoolResponseSerializer(r).data)
class CompanySchoolListView(APIView):
    def get(self,request,company_id): return Response(SchoolResponseSerializer(services()['school'].list(ListCompanySchoolsQuery(company_id)),many=True).data)
