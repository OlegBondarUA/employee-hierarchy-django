from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator

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


def employee_list(request):
    sort_by = request.GET.get('sort_by', 'id')
    search_query = request.GET.get('search', '')

    employees = Employee.objects.all().order_by(sort_by)
    if search_query:
        employees = employees.filter(full_name__icontains=search_query)

    paginator = Paginator(employees, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'employees/employee_list_ajax.html', {'page_obj': page_obj})

    return render(request, 'employees/employee_list.html', {'page_obj': page_obj, 'sort_by': sort_by})