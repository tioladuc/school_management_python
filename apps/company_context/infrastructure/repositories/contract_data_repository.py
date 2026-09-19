from ..orm.models import ContractDataModel
from ..mappers.contract_data_mapper import ContractDataMapper
class ContractDataRepository:
    def save(self, data):
        obj=ContractDataModel.objects.filter(pk=data.id).first() if data.id else ContractDataModel()
        ContractDataMapper.to_model(data,obj);obj.save();return ContractDataMapper.to_domain(obj)
    def list_for_contract(self, contract_id): return [ContractDataMapper.to_domain(x) for x in ContractDataModel.objects.filter(contract_id=contract_id).order_by('-transaction_date','-id')]
    def list_for_company(self, company_id): return [ContractDataMapper.to_domain(x) for x in ContractDataModel.objects.filter(contract__company_id=company_id).order_by('-transaction_date','-id')]
