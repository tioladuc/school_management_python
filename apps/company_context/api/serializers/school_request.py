from rest_framework import serializers
class CreateSchoolRequestSerializer(serializers.Serializer):
    company_id=serializers.IntegerField()
    code=serializers.CharField(max_length=50)
    name=serializers.CharField(max_length=250)
    city=serializers.CharField(max_length=150)
    country=serializers.CharField(max_length=100)
class UpdateSchoolRequestSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=250);city=serializers.CharField(max_length=150);country=serializers.CharField(max_length=100)
