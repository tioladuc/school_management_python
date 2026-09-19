from ..orm.models import StaffModel
from ..mappers.staff_mapper import StaffMapper
class StaffRepository:
    def get(self, staff_id):
        try:return StaffMapper.to_domain(StaffModel.objects.get(pk=staff_id))
        except StaffModel.DoesNotExist:return None
    def save(self, staff):
        obj=StaffModel.objects.filter(pk=staff.id).first() if staff.id else StaffModel()
        StaffMapper.to_model(staff,obj);obj.save();staff.id=obj.id;return StaffMapper.to_domain(obj)
    def exists_by_number(self, company_id, staff_number): return StaffModel.objects.filter(company_id=company_id,staff_number=staff_number.strip()).exists()
    def search(self, company_id, search=''):
        qs=StaffModel.objects.filter(company_id=company_id)
        if search: qs=qs.filter(first_name__icontains=search)|qs.filter(last_name__icontains=search)|qs.filter(staff_number__icontains=search)
        return [StaffMapper.to_domain(x) for x in qs.order_by('last_name','first_name')]
