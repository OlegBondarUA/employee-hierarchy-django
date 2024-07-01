from django.urls import path
from . import views

urlpatterns = [
    path('employee_hierarchy/', views.employee_hierarchy, name='employee_hierarchy'),
]