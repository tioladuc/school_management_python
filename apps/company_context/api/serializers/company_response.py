from rest_framework import serializers
class CompanyResponseSerializer(serializers.Serializer):
    id=serializers.IntegerField();code=serializers.CharField();name=serializers.CharField();email=serializers.EmailField();phone=serializers.CharField();address=serializers.CharField();status=serializers.CharField();school_count=serializers.IntegerField()
