from ..orm.models import CompanyModel
from ..mappers.company_mapper import CompanyMapper


class CompanyRepository:
    def get(self, company_id):
        try:
            return CompanyMapper.to_domain(CompanyModel.objects.get(pk=company_id))
        except CompanyModel.DoesNotExist:
            return None

    def save(self, company):
        obj = (
            CompanyModel.objects.filter(pk=company.id).first()
            if company.id
            else CompanyModel()
        )
        CompanyMapper.to_model(company, obj)
        obj.save()
        company.id = obj.id
        return CompanyMapper.to_domain(obj)

    def exists_by_code(self, code):
        return CompanyModel.objects.filter(code=code.strip().upper()).exists()

    def search(self, search="", status=None):
        # qs = CompanyModel.objects.all()
        # if search:
        #     qs = qs.filter(name__icontains=search) | qs.filter(code__icontains=search)
        # if status:
        #     qs = qs.filter(status=status)
        sample_companies = [
            {
                "id": "1",
                "code": "COMP001",
                "name": "Learning Kids Québec",
                "email": "contact@learningkids.ca",
                "phone": "514-555-1001",
                "address": "123 Rue Sainte-Catherine, Montréal, QC, Canada",
                "status": "ACTIVE",
                "tenant_database": "tenant_comp001",
            },
            {
                "id": "2",
                "code": "COMP002",
                "name": "Montreal Academy",
                "email": "info@montrealacademy.ca",
                "phone": "514-555-1002",
                "address": "456 Boulevard René-Lévesque, Montréal, QC, Canada",
                "status": "ACTIVE",
                "tenant_database": "tenant_comp002",
            },
            {
                "id": "3",
                "code": "COMP003",
                "name": "Quebec Education Group",
                "email": "admin@qeg.ca",
                "phone": "418-555-1003",
                "address": "789 Grande Allée, Québec, QC, Canada",
                "status": "ACTIVE",
                "tenant_database": "tenant_comp003",
            },
            {
                "id": "4",
                "code": "COMP004",
                "name": "Northern Schools Inc.",
                "email": "contact@northernschools.ca",
                "phone": "204-555-1004",
                "address": "100 Main Street, Winnipeg, MB, Canada",
                "status": "SUSPENDED",
                "tenant_database": "tenant_comp004",
            },
            {
                "id": "5",
                "code": "COMP005",
                "name": "Prairie Learning Center",
                "email": "info@prairielearning.ca",
                "phone": "780-555-1005",
                "address": "200 Jasper Avenue, Edmonton, AB, Canada",
                "status": "ACTIVE",
                "tenant_database": "tenant_comp005",
            },
            {
                "id": "6",
                "code": "COMP006",
                "name": "Alberta Education Services",
                "email": "contact@abeducation.ca",
                "phone": "403-555-1006",
                "address": "300 8 Avenue SW, Calgary, AB, Canada",
                "status": "TERMINATED",
                "tenant_database": "tenant_comp006",
            },
        ]
        # return [CompanyMapper.to_domain(x) for x in qs.order_by("name")]
        return [CompanyMapper.to_domain(x) for x in sample_companies]