# Employee Management

A Django project I built. It's an employee directory where HR can add, edit and delete employees. Other people can only see their own details, and managers can also see their team.

I started with function based views and later changed everything to class based views and added roles and permissions.

## What it does

- Employee list, detail, add, update and delete
- Departments, and every employee can have a manager (a manager is also an employee)
- Login and logout using Django's built in views
- Register page (new accounts have no permissions until an admin adds them to a group)
- Roles using Django groups: HR, Manager and Employee
- Each login can be linked to one employee record
- Secret key and debug settings are kept in a `.env` file
- Admin panel with import/export (django-import-export)

## Roles

| Role | What they can do |
|------|------------------|
| HR | See all employees, add, edit, delete |
| Manager | See their own record and their team (view only) |
| Employee | See only their own record (view only) |

A superuser can do everything.

## Tech stack

- Python 3, Django
- SQLite
- Pillow, django-import-export, python-decouple
- HTML, CSS, Bootstrap 5

## Project structure

```
Django/
├── Employee_App/     # project settings and root urls
├── accounts/         # register, login, logout
├── employees/        # models, views, forms, admin
├── templates/        # html templates
├── static/css/       # custom css
├── media/emp_images/ # uploaded photos and default avatar
└── manage.py
```

## How to run

```bash
# 1. clone
git clone https://github.com/Deep-py23/Employee-Management.git
cd Employee-Management/Django

# 2. virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. install packages
pip install -r requirements.txt
```

4. Create a file called `.env` next to `manage.py` and add:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

You can generate a key with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

```bash
# 5. create the database
python manage.py migrate

# 6. create an admin user
python manage.py createsuperuser

# 7. run the server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in the browser.


## What I learned

- Function views vs class based views
- `PermissionRequiredMixin` and Django groups and permissions
- Filtering rows with `get_queryset` and `Q` objects
- `select_related` to avoid N+1 database queries
- Keeping secrets out of GitHub with a `.env` file

## Things I want to add next

- Tests
- Validation (a manager can't be their own manager, salary must be positive)
- Approval for new registrations
- Success messages after add, edit and delete
- Search and pagination