import random
from datetime import date
from django.core.management.base import BaseCommand
from employees.models import Employee


class Command(BaseCommand):
    help = 'Populate the database with employee data'

    def handle(self, *args, **kwargs):
        Employee.objects.all().delete()

        self.populate_employees()

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))

    def populate_employees(self):
        positions = ['Manager', 'Developer', 'Designer', 'QA Engineer', 'Project Manager']
        domains = ['example.com', 'test.com', 'company.com']

        for i in range(1, 50001):
            full_name = f'Employee {i}'
            position = random.choice(positions)
            hire_date = date.today()
            email = f'employee{i}@{random.choice(domains)}'

            if i == 1:
                manager = None
            else:
                manager = Employee.objects.get(pk=random.randint(1, i - 1))

            Employee.objects.create(
                full_name=full_name,
                position=position,
                hire_date=hire_date,
                email=email,
                manager=manager
            )
