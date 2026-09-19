from django.test import SimpleTestCase
from ..api.serializers.company_request import CreateCompanyRequestSerializer
from ..api.serializers.contract_request import CreateContractRequestSerializer
class SerializerTests(SimpleTestCase):
    def test_company_request_validates_email(self):
        self.assertFalse(CreateCompanyRequestSerializer(data={'code':'ABC','name':'ABC','email':'bad'}).is_valid())
    def test_contract_dates(self):
        data={'company_id':1,'signature_date':'2026-01-01','company_setup_price':'1','school_setup_price':'2','academic_year_renewal_price':'3','start_date':'2026-01-01','end_date':'2025-01-01'}
        self.assertFalse(CreateContractRequestSerializer(data=data).is_valid())
