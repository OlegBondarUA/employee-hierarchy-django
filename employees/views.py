from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employee


def employee_hierarchy(request):
    root_employees = Employee.objects.filter(manager__isnull=True)[:10]
    return render(request, 'employees/employee_hierarchy.html', {'root_employees': root_employees})


def load_subordinates(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    subordinates = employee.subordinates.all()[:10]
    data = {
        'html': ''.join(
            f'<li data-employee-id="{subordinate.id}">{subordinate.full_name} ({subordinate.position})'
            f'<ul class="subordinates"></ul>'
            f'<button class="load-more" data-employee-id="{subordinate.id}">Load more...</button>'
            f'</li>'
            for subordinate in subordinates
        )
    }
    return JsonResponse(data)