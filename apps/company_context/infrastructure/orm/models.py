from django.db import models

class CompanyModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    code=models.CharField(max_length=50, unique=True)
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone=models.CharField(max_length=50, blank=True)
    address=models.TextField(blank=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    tenant_database=models.CharField(max_length=150, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: db_table='company'

class SchoolModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='schools')
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=250)
    city=models.CharField(max_length=150)
    country=models.CharField(max_length=100)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='school'
        constraints=[models.UniqueConstraint(fields=['company','code'],name='uq_school_company_code')]

class StaffModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='staff')
    staff_number=models.CharField(max_length=80)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=50,blank=True)
    position=models.CharField(max_length=150,blank=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='staff'
        constraints=[models.UniqueConstraint(fields=['company','staff_number'],name='uq_staff_company_number')]

class ContractModel(models.Model):
    STATUS_CHOICES=[('DRAFT','Draft'),('ACTIVE','Active'),('SUSPENDED','Suspended'),('TERMINATED','Terminated')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='contracts')
    signature_date=models.DateField()
    company_setup_price=models.DecimalField(max_digits=14,decimal_places=2)
    school_setup_price=models.DecimalField(max_digits=14,decimal_places=2)
    academic_year_renewal_price=models.DecimalField(max_digits=14,decimal_places=2)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='DRAFT')
    currency=models.CharField(max_length=3,default='CAD')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: db_table='contract'

class ContractDataModel(models.Model):
    TRANSACTION_TYPES=[('COMPANY_CREATION','Company creation'),('SCHOOL_CREATION','School creation'),('ACADEMIC_YEAR_RENEWAL','Academic year renewal'),('CUSTOM_FEE','Custom fee'),('DISCOUNT','Discount'),('CREDIT_NOTE','Credit note')]
    contract=models.ForeignKey(ContractModel,on_delete=models.PROTECT,related_name='billing_data')
    transaction_type=models.CharField(max_length=40,choices=TRANSACTION_TYPES)
    transaction_date=models.DateField()
    quantity=models.DecimalField(max_digits=14,decimal_places=3)
    unit_price=models.DecimalField(max_digits=14,decimal_places=2)
    total_amount=models.DecimalField(max_digits=14,decimal_places=2)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: db_table='contract_data'

class SubscriptionModel(models.Model):
    STATUS_CHOICES=[('ACTIVE','Active'),('SUSPENDED','Suspended'),('CANCELLED','Cancelled')]
    company=models.ForeignKey(CompanyModel,on_delete=models.PROTECT,related_name='subscriptions')
    plan_code=models.CharField(max_length=80)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='ACTIVE')
    class Meta: db_table='subscription'
