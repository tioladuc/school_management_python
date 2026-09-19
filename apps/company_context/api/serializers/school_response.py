from rest_framework import serializers
class SchoolResponseSerializer(serializers.Serializer):
    id=serializers.IntegerField();company_id=serializers.IntegerField();code=serializers.CharField();name=serializers.CharField();city=serializers.CharField();country=serializers.CharField();status=serializers.CharField()
