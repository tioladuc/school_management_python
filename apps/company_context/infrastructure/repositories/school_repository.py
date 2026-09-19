from ..orm.models import SchoolModel
from ..mappers.school_mapper import SchoolMapper
class SchoolRepository:
    def get(self, school_id):
        try:return SchoolMapper.to_domain(SchoolModel.objects.get(pk=school_id))
        except SchoolModel.DoesNotExist:return None
    def save(self, school):
        obj=SchoolModel.objects.filter(pk=school.id).first() if school.id else SchoolModel()
        SchoolMapper.to_model(school,obj);obj.save();school.id=obj.id;return SchoolMapper.to_domain(obj)
    def exists_by_code(self, company_id, code): return SchoolModel.objects.filter(company_id=company_id,code=code.strip().upper()).exists()
    def list_by_company(self, company_id): return [SchoolMapper.to_domain(x) for x in SchoolModel.objects.filter(company_id=company_id).order_by('name')]
