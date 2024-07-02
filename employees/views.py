from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import Employee
from .forms import EmployeeForm


def employee_hierarchy(request):
    root_employees = Employee.objects.filter(manager__isnull=True)[:5]
    return render(request, 'employees/employee_hierarchy.html', {'root_employees': root_employees})


def load_subordinates(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    subordinates = employee.subordinates.all()[:10]

    html = ''.join(
        f'<li class="list-group-item" data-employee-id="{subordinate.id}">'
        f'<div class="employee-header">'
        f'<strong>{subordinate.full_name}</strong> ({subordinate.position})'
        f'</div>'
        f'<ul class="list-group list-group-flush ms-3 subordinates"></ul>'
        f'<button class="btn btn-primary btn-sm load-more mt-2" data-employee-id="{subordinate.id}">Load more...</button>'
        f'</li>'
        for subordinate in subordinates
    )

    data = {'html': html}
    return JsonResponse(data)


def reassign_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    new_manager_id = request.POST.get('new_manager_id')
    if new_manager_id:
        new_manager = get_object_or_404(Employee, id=new_manager_id)
        employee.manager = new_manager
        employee.save()
        return JsonResponse({'message': 'Employee reassigned successfully'})
    else:
        return JsonResponse({'error': 'New manager ID not provided'}, status=400)


@login_required
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

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Співробітника створено успішно.')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Інформацію про співробітника оновлено успішно.')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Співробітника видалено успішно.')
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш акаунт створено! Тепер ви можете увійти.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_success(request):
    return render(request, 'users/login_success.html')
