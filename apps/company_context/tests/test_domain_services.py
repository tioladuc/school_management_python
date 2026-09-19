from datetime import date, timedelta
from decimal import Decimal
from django.test import SimpleTestCase
from ..domain.entities.company import Company
from ..domain.entities.contract import Contract
from ..domain.entities.school import School
from ..domain.services.school_registration_service import SchoolRegistrationService
from ..domain.services.contract_billing_service import ContractBillingService
from ..domain.value_objects.company_code import CompanyCode
from ..domain.exceptions import BusinessRuleError

class CompanyContextDomainTests(SimpleTestCase):
    def company(self): return Company(1,CompanyCode('ABC'), 'ABC Education','a@example.com')
    def contract(self, status='ACTIVE'):
        return Contract(1,1,date.today(),Decimal('500'),Decimal('150'),Decimal('50'),date.today()-timedelta(days=1),date.today()+timedelta(days=365),status)
    def test_school_requires_active_contract(self):
        with self.assertRaises(BusinessRuleError): SchoolRegistrationService().register(self.company(),School(None,1,'S1','School','Montreal','Canada'),self.contract('SUSPENDED'))
    def test_school_registration_allowed_when_company_and_contract_active(self):
        school=SchoolRegistrationService().register(self.company(),School(None,1,'S1','School','Montreal','Canada'),self.contract())
        self.assertEqual(school.code,'S1')
    def test_school_billing_uses_contract_price(self):
        data=ContractBillingService().bill_school_creation(self.contract(),2)
        self.assertEqual(data.total_amount,Decimal('300'))
        self.assertEqual(data.transaction_type,'SCHOOL_CREATION')
