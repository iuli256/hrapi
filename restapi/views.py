from restapi.models import Employee
from rest_framework import viewsets
from restapi.serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
import pandas as pd
from datetime import date


class StatisticsAvgAgPerIndView(viewsets.ViewSet):
    """
    API endpoint that show average age per industry.
    """

    def list(self, request):
        def age(born):
            today = date.today()
            return today.year - born.year - ((today.month,
                                              today.day) < (born.month,
                                                            born.day))

        lst_employee = Employee.objects.all().values()
        df = pd.DataFrame(lst_employee)
        df['age'] = df['date_of_birth'].apply(age)

        return Response(df.groupby('industry')['age'].mean().round(2).to_dict())


class StatisticsAvgSalPerIndView(viewsets.ViewSet):
    """
    API endpoint that show average salary per industry.
    """

    def list(self, request):

        lst_employee = Employee.objects.all().values()
        df = pd.DataFrame(lst_employee)

        return Response(df.groupby('industry')['salary'].mean().round(2).to_dict())


class StatisticsAvgSalPerExpView(viewsets.ViewSet):
    """
    API endpoint that show average salary per years of experience.
    """

    def list(self, request):

        lst_employee = Employee.objects.all().values()
        df = pd.DataFrame(lst_employee)

        return Response(df.groupby('years_of_experience')['salary'].mean().round(2).to_dict())


class StatisticsAvgAgPerGenAndExpView(viewsets.ViewSet):
    """
    API endpoint that show average salary per gender and years of experience.
    """

    def list(self, request):

        lst_employee = Employee.objects.all().values()
        df = pd.DataFrame(lst_employee)
        grouped_multiple = df.groupby(['gender', 'years_of_experience']).agg({'salary': ['mean', 'min', 'max']})
        grouped_multiple.columns = ['salary_mean', 'salary_min', 'salary_max']
        grouped_multiple = grouped_multiple.reset_index()

        return Response(grouped_multiple.round(2).to_dict(orient='records'))


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be searched, viewed, edited or deleted.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name', 'id']
    ordering = ['id']