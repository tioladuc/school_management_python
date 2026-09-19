from ..orm.models import ContractModel
from ..mappers.contract_mapper import ContractMapper
class ContractRepository:
    def get(self, contract_id):
        try:return ContractMapper.to_domain(ContractModel.objects.get(pk=contract_id))
        except ContractModel.DoesNotExist:return None
    def save(self, contract):
        obj=ContractModel.objects.filter(pk=contract.id).first() if contract.id else ContractModel()
        ContractMapper.to_model(contract,obj);obj.save();contract.id=obj.id;return ContractMapper.to_domain(obj)
    def get_active_for_company(self, company_id):
        obj=ContractModel.objects.filter(company_id=company_id,status='ACTIVE').order_by('-start_date').first()
        return ContractMapper.to_domain(obj) if obj else None
    def list_for_company(self, company_id): return [ContractMapper.to_domain(x) for x in ContractModel.objects.filter(company_id=company_id).order_by('-start_date')]
