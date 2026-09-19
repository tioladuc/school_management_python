from ..orm.models import CompanyModel
from ..mappers.company_mapper import CompanyMapper
class CompanyRepository:
    def get(self, company_id):
        try: return CompanyMapper.to_domain(CompanyModel.objects.get(pk=company_id))
        except CompanyModel.DoesNotExist: return None
    def save(self, company):
        obj=CompanyModel.objects.filter(pk=company.id).first() if company.id else CompanyModel()
        CompanyMapper.to_model(company,obj);obj.save();company.id=obj.id;return CompanyMapper.to_domain(obj)
    def exists_by_code(self, code): return CompanyModel.objects.filter(code=code.strip().upper()).exists()
    def search(self, search='', status=None):
        qs=CompanyModel.objects.all()
        if search: qs=qs.filter(name__icontains=search)|qs.filter(code__icontains=search)
        if status: qs=qs.filter(status=status)
        return [CompanyMapper.to_domain(x) for x in qs.order_by('name')]
