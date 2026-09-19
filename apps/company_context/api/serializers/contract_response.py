from rest_framework import serializers
class ContractResponseSerializer(serializers.Serializer):
    id=serializers.IntegerField();company_id=serializers.IntegerField();signature_date=serializers.DateField();company_setup_price=serializers.DecimalField(max_digits=14,decimal_places=2);school_setup_price=serializers.DecimalField(max_digits=14,decimal_places=2);academic_year_renewal_price=serializers.DecimalField(max_digits=14,decimal_places=2);start_date=serializers.DateField();end_date=serializers.DateField();status=serializers.CharField();currency=serializers.CharField()
