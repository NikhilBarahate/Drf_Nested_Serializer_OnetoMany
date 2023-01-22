from django.shortcuts import render
from rest_framework import generics
from app1.models import Employee, Project
from app1.serializers import EmployeeSerializer, ProjectSerializer

# Create your views here.
class Employee_info(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Employee_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class Project_info(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
