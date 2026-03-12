# Skill Tracker

A Django web application for tracking skills and habits.

## Features

- Create, edit and delete skills with categories
- Create, edit and delete habits linked to skills
- Profile management
- Responsive design with Bootstrap 5

## Technologies

- Python 3.10+
- Django 5.x
- PostgreSQL
- Bootstrap 5
- Crispy Forms

## Database Relationships

- **Profile → Skills**: One-to-Many (ForeignKey)
- **Habit ↔ Skills**: Many-to-Many

## Installation

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Configure PostgreSQL in `skilltrack/settings.py`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
7. Open http://localhost:8000

## Author

Viktor Tahmisyan