from rest_framework import serializers
from .models import Employee  # Import your Employee model

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id","name","empid","company"]
