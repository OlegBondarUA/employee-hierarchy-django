from django.shortcuts import render
from .models import Employee


def employee_hierarchy(request):
    root_employees = Employee.objects.filter(manager__isnull=True)

    context = {
        'root_employees': root_employees,
    }
    return render(request, 'employees/employee_hierarchy.html', context)
