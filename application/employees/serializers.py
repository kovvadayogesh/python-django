from rest_framework import serializers
from . models import Employee,EmployeeDetails



class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    
class EmployeeDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'