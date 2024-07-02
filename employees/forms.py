from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from employees.models import Employee


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'hire_date', 'email', 'manager']