from rest_framework import serializers
class StaffResponseSerializer(serializers.Serializer):
    id=serializers.IntegerField();company_id=serializers.IntegerField();staff_number=serializers.CharField();first_name=serializers.CharField();last_name=serializers.CharField();email=serializers.EmailField();phone=serializers.CharField();position=serializers.CharField();status=serializers.CharField()
