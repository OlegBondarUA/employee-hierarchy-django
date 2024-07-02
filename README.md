Проєкт "Employee Hierarchy Django"

Цей проєкт реалізує веб-додаток для відображення ієрархії співробітників з можливістю сортування та пагінації.

1. Клонування проєкту

    Для початку, клонуйте репозиторій з GitHub за допомогою команди:

    ```bash
    git clone https://github.com/OlegBondarUA/employee-hierarchy-django.git

2. Встановлення віртуального середовища

    Переконайтеся, що встановлено Python та virtualenv:

    ```bash
    python3 -m venv venv
   
3. Активуйте віртуальне середовище:
    ```bash
    # На Windows
    venv\Scripts\activate
    # На macOS або Linux
    source venv/bin/activate

4. Встановлення залежностей

    Перейдіть до каталогу проєкту та встановіть необхідні бібліотеки з файлу requirements.txt:
    ```bash
    cd employee-hierarchy-django
    pip install -r requirements.txt
   
5. Запуск проєкту Django

    Застосуйте міграції та запустіть сервер Django:
    ```bash
    python manage.py migrate
    python manage.py runserver
Проєкт буде доступний за адресою http://localhost:8000/.

6. Заповніть базу данних
    ```bash
    python manage.py seed_db       
   
7. Створіть суперкористувача Django:

    ```bash
   python manage.py createsuperuser
   
Введіть ім'я користувача, електронну пошту та пароль за інструкціями на екрані.

Тепер ви маєте повний доступ до усіх можливостей проєкту.