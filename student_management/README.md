# Student Management System (Django)

A simple Django project with two apps — **student** and **professor** —
demonstrating models, admin, views, URL routing, and templates.

## Structure

```
student_management_system/
├── manage.py
├── requirements.txt
├── db.sqlite3                   # pre-seeded with sample data
├── studentmgmt/                  # project settings
│   ├── settings.py
│   ├── urls.py                   # root urls -> home, student/, professor/
│   └── views.py                  # home() view
├── student/                       # STUDENT APP
│   ├── models.py                 # Student model
│   ├── admin.py
│   ├── views.py                  # student_list view
│   ├── urls.py
│   └── management/commands/seed_data.py
├── professor/                     # PROFESSOR APP
│   ├── models.py                 # Professor + Subject models
│   ├── admin.py
│   ├── views.py                  # professor_list view (professors + subjects)
│   └── urls.py
└── templates/
    ├── base.html                 # shared layout & styling
    ├── home.html                 # 2 app options
    ├── student/student_list.html
    └── professor/professor_list.html
```

## Run it

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data      # optional: loads sample students/professors/subjects
python manage.py runserver
```

Open **http://127.0.0.1:8000/** — you'll see two options: Student and Professor.

- **Student** → table of all students, with a Back button.
- **Professor** → table of professors + table of subjects (each subject linked to its professor), with a Back button.

## Admin panel

A superuser is already created for local testing:

- URL: http://127.0.0.1:8000/admin/
- Username: `admin`
- Password: `admin123`

Use the admin panel to add/edit/delete Student, Professor, and Subject records —
they'll immediately show up on the site.

## Models

**Student** (`student/models.py`)
- roll_no, name, email, course, year, phone

**Professor** (`professor/models.py`)
- emp_id, name, email, department, phone

**Subject** (`professor/models.py`)
- code, name, credits, professor (ForeignKey → Professor)
