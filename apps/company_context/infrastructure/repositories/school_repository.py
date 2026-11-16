from config import settings

from ..orm.models import SchoolModel
from ..mappers.school_mapper import SchoolMapper


class SchoolRepository:

    def __init__(self, connection_alias):
        self.connection_alias = connection_alias

    
    def get_all(self, db_alias="default"):
        return SchoolModel.objects.using(db_alias).all()



    def get_by_id(self, school_id, db_alias="default"):
        return SchoolModel.objects.using(db_alias).filter(
            id=school_id
        ).first()



    def create(self, data, db_alias="default"):
        return SchoolModel.objects.using(db_alias).create(**data)



    def saveBeta(self, school_id, data, db_alias="default"):
        if school_id:
            obj = (
                SchoolModel.objects.using(db_alias)
                .filter(pk=school_id)
                .first()
            )
            
            if obj is None:
                raise ValueError(f"School {school_id} does not exist.")
            
        else:
            obj = SchoolModel()
            
        SchoolMapper.to_model(data, obj)
        obj.save(using=db_alias)        
        return SchoolMapper.to_domain(obj)



    def update(self, school_id, data, db_alias="default"):
        obj = (
                    SchoolModel.objects.using(db_alias).filter(pk=school_id).first()
                    if school_id
                    else SchoolModel()
                )
        SchoolMapper.to_model(data, obj)
        obj.save(using=db_alias)


    def delete(self, school_id, db_alias="default"):
        return SchoolModel.objects.using(db_alias).filter(
            id=school_id
        ).delete()


    def get(self, school_id):
        try:
            obj = SchoolModel.objects.using(self.connection_alias).get(pk=school_id)

            return SchoolMapper.to_domain(obj)

        except SchoolModel.DoesNotExist:
            return None



    def save(self, school):
        manager = SchoolModel.objects.using(self.connection_alias)

        if school.id:
            obj = manager.filter(pk=school.id).first()
        else:
            obj = SchoolModel()

        SchoolMapper.to_model(school, obj)
        obj.save(using=self.connection_alias)
        school.id = obj.id

        return SchoolMapper.to_domain(obj)



    def exists_by_code(self, company_id, code):
        return (
            SchoolModel.objects.using(self.connection_alias)
            .filter(company_id=company_id, code=code.strip().upper())
            .exists()
        )



    def list_by_company(self, company_id):
        schools = (
            SchoolModel.objects.using(self.connection_alias)
            .filter(company_id=company_id)
            .order_by("name")
        )

        return [SchoolMapper.to_domain(school) for school in schools]
