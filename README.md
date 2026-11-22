# Employee Management

A Django web app for managing employees, with full CRUD, user accounts, profile image uploads and a clean Bootstrap-based interface.

## Features

- **Employee CRUD**: add, view, edit and delete employees
- **Employee detail page** with profile photo and all details
- **Delete confirmation** page so nothing is removed by accident
- **Departments and managers**: each employee can belong to a department and report to another employee
- **Profile images** with a default avatar when none is uploaded
- **User accounts**: register, login and logout
- **Responsive UI** built with Bootstrap 5, Font Awesome icons and custom CSS
- **Flash messages** for user feedback

## Tech Stack

- Python 3, Django
- SQLite (default Django database)
- HTML, CSS, Bootstrap 5

## Project Structure

```
Django/
├── Employee_App/     # project settings and root URLs
├── accounts/         # register / login / logout
├── employees/        # Employee and Department models, views, forms
├── templates/        # HTML templates (base, list, detail, forms, accounts)
├── static/css/       # custom stylesheet
├── media/emp_images/ # uploaded profile images and default avatar
└── manage.py
```

## Setup

```bash
# 1. Clone the repository
git clone https://github.com/Deep-py23/Employee-Management.git
cd Employee-Management/Django

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the database tables
python manage.py migrate

# 5. (Optional) Create an admin user
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.


