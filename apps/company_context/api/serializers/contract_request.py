from rest_framework import serializers
class CreateContractRequestSerializer(serializers.Serializer):
    company_id=serializers.IntegerField();signature_date=serializers.DateField();company_setup_price=serializers.DecimalField(max_digits=14,decimal_places=2);school_setup_price=serializers.DecimalField(max_digits=14,decimal_places=2);academic_year_renewal_price=serializers.DecimalField(max_digits=14,decimal_places=2);start_date=serializers.DateField();end_date=serializers.DateField();currency=serializers.CharField(max_length=3,default='CAD')
    def validate(self,data):
        if data['end_date'] <= data['start_date']: raise serializers.ValidationError('end_date must be later than start_date.')
        return data
class UpdateContractRequestSerializer(CreateContractRequestSerializer): pass
