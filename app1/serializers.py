from pyexpat import model
from rest_framework import serializers
from app1.models import Employee, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    emp_project = ProjectSerializer(read_only=True, many=True)
    class Meta:
        model = Employee
        fields = '__all__'