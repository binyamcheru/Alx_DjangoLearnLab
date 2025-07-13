# LibraryProject

A Django project for managing a library system. This project includes a bookshelf app for managing books.

## Setup

1. Install Django: `pip install django`
2. Navigate to project directory: `cd LibraryProject`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Start development server: `python manage.py runserver`

## Apps

- **bookshelf**: Manages book records with CRUD operations

## Models

- **Book**: Contains title, author, and publication year fields

## Admin Interface

The Django admin interface is configured to manage Book models with:
- List view showing title, author, and publication year
- Search functionality by title and author
- Filtering by publication year