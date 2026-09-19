from rest_framework import serializers
class ContractDataResponseSerializer(serializers.Serializer):
    id=serializers.IntegerField();contract_id=serializers.IntegerField();transaction_type=serializers.CharField();transaction_date=serializers.DateField();quantity=serializers.DecimalField(max_digits=14,decimal_places=3);unit_price=serializers.DecimalField(max_digits=14,decimal_places=2);total_amount=serializers.DecimalField(max_digits=14,decimal_places=2);description=serializers.CharField()
