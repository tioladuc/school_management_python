from rest_framework import serializers
class CreateStaffRequestSerializer(serializers.Serializer):
    company_id=serializers.IntegerField();staff_number=serializers.CharField(max_length=80);first_name=serializers.CharField(max_length=150);last_name=serializers.CharField(max_length=150);email=serializers.EmailField();phone=serializers.CharField(max_length=50,required=False,allow_blank=True);position=serializers.CharField(max_length=150,required=False,allow_blank=True)
class UpdateStaffRequestSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=150);last_name=serializers.CharField(max_length=150);email=serializers.EmailField();phone=serializers.CharField(max_length=50,required=False,allow_blank=True);position=serializers.CharField(max_length=150,required=False,allow_blank=True)
