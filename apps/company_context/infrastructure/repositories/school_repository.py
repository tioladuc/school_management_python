# from ..orm.models import SchoolModel
# from ..mappers.school_mapper import SchoolMapper
# class SchoolRepository:
#    def get(self, school_id):
#        try:return SchoolMapper.to_domain(SchoolModel.objects.get(pk=school_id))
#        except SchoolModel.DoesNotExist:return None
#    def save(self, school):
#        obj=SchoolModel.objects.filter(pk=school.id).first() if school.id else SchoolModel()
#        SchoolMapper.to_model(school,obj);obj.save();school.id=obj.id;return SchoolMapper.to_domain(obj)
#    def exists_by_code(self, company_id, code): return SchoolModel.objects.filter(company_id=company_id,code=code.strip().upper()).exists()
#    def list_by_company(self, company_id): return [SchoolMapper.to_domain(x) for x in SchoolModel.objects.filter(company_id=company_id).order_by('name')]


from config import settings

from ..orm.models import SchoolModel
from ..mappers.school_mapper import SchoolMapper


class SchoolRepository:

    def __init__(self, connection_alias):
        self.connection_alias = connection_alias

    
    def get_all(self, db_alias="default"):
        print(db_alias, 'Getting all schools from the database UUUUUUUUUUUUUUUUUUUUUUU')
        print(settings.DATABASES, 'DATABASES')
        return SchoolModel.objects.using(db_alias).all()

    def get_by_id(self, school_id, db_alias="default"):
        return SchoolModel.objects.using(db_alias).filter(
            id=school_id
        ).first()

    def create(self, data, db_alias="default"):
        return SchoolModel.objects.using(db_alias).create(**data)

    def saveBeta(self, school_id, data, db_alias="default"):
        print('0000000000000000000000')
        if school_id:
            print('2222222222222222222222')
            obj = (
                SchoolModel.objects.using(db_alias)
                .filter(pk=school_id)
                .first()
            )
            print('11111111111111111111111')
            if obj is None:
                raise ValueError(f"School {school_id} does not exist.")
            print('5555555555555555555555')

        else:
            print('3333333333333333333333')
            obj = SchoolModel()
            print('4444444444444444444444')

        print('666666666666666666666')
        SchoolMapper.to_model(data, obj)
        print('777777777777777777777777')
        obj.save(using=db_alias)
        print('88888888888888888888888')

        return SchoolMapper.to_domain(obj)

    def update(self, school_id, data, db_alias="default"):
        print('EEEEEEEEEEEEEEEEEEEEEEEEE')
        obj = (
                    SchoolModel.objects.using(db_alias).filter(pk=school_id).first()
                    if school_id
                    else SchoolModel()
                )
        print('DUDUDUDUDUDUDUDUDDUDUDDU')
        print(data)
        print('YYYYYYYYYYYYYYYYYYYYY')
        print(obj.id)
        print('RRRRRRRRRRRRRRRRRRRR')
        SchoolMapper.to_model(data, obj)
        print('KKKKKKKOKOKOKOKOKOKO')
        obj.save(using=db_alias)
        #return SchoolModel.objects.using(db_alias).filter(
        #    id=school_id
        #).update(obj)

    def delete(self, school_id, db_alias="default"):
        return SchoolModel.objects.using(db_alias).filter(
            id=school_id
        ).delete()


    # ===================================================================
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
