from restapi.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'industry', 'salary', 'years_of_experience']