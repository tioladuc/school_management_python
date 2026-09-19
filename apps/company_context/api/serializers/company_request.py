from rest_framework import serializers
class CreateCompanyRequestSerializer(serializers.Serializer):
    code=serializers.CharField(max_length=50)
    name=serializers.CharField(max_length=250)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=50,required=False,allow_blank=True)
    address=serializers.CharField(required=False,allow_blank=True)

class UpdateCompanyRequestSerializer(CreateCompanyRequestSerializer): pass
