from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.employee_hierarchy, name='employee_hierarchy'),
    path('load_subordinates/<int:employee_id>/', views.load_subordinates, name='load_subordinates'),
    path('reassign_employee/<int:employee_id>/', views.reassign_employee, name='reassign_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login_success/', views.login_success, name='login_success'),
]

