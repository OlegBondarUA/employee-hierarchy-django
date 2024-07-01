from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_hierarchy, name='employee_hierarchy'),
    path('load_subordinates/<int:employee_id>/', views.load_subordinates, name='load_subordinates'),
    path('employee_list/', views.employee_list, name='employee_list'),
]

