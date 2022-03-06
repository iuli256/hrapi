"""djangoRestAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'statistics/average_age_per_industry',
                views.StatisticsAvgAgPerIndView,
                basename='average_age_per_industry')
router.register(r'statistics/average_salaries_per_industry',
                views.StatisticsAvgSalPerIndView,
                basename='average_salaries_per_industry')
router.register(r'statistics/average_salaries_per_years_of_experience',
                views.StatisticsAvgSalPerExpView,
                basename='average_salaries_per_years_of_experience')
router.register(r'statistics/average_salaries_per_gender_and_experience',
                views.StatisticsAvgAgPerGenAndExpView,
                basename='average_salaries_per_gender_and_experience')
urlpatterns = [
    path('', include(router.urls)),
#    path('statistics/<str:report>', views.StatisticsView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
