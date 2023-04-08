from rest_framework import serializers
from .models import Employe
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['id', 'name', 'emp_id', 'position', 'email', 'mobile']
        extra_kwargs = {'name': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'emp_id': {'required': True,'allow_blank': False}}
        extra_kwargs = {'postion': {'required': True,'allow_blank': False}}
