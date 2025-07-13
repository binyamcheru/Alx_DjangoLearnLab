# CRUD Operations Documentation

This document contains all the CRUD (Create, Read, Update, Delete) operations performed on the Book model using Django's ORM through the Django shell.

## Prerequisites
Before running these operations, ensure:
1. Django project is set up
2. Bookshelf app is created and added to INSTALLED_APPS
3. Book model is defined in bookshelf/models.py
4. Migrations are created and applied
5. Django shell is opened with: `python manage.py shell`

## Create Operation

### Command
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell", 
    publication_year=1949
)
print(f"Created book: {book}")
```

### Output
```
Created book: 1984 by George Orwell (1949)
```

## Retrieve Operation

### Command
```python
# Retrieve the book we created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"Book ID: {book.id}")
```

### Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
Book ID: 1
```

## Update Operation

### Command
```python
# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated book: {book}")
print(f"New title: {book.title}")
```

### Output
```
Updated book: Nineteen Eighty-Four by George Orwell (1949)
New title: Nineteen Eighty-Four
```

## Delete Operation

### Command
```python
# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book_title = book.title
book.delete()

print(f"Deleted book: {book_title}")

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Remaining books: {all_books}")
print(f"Total books count: {all_books.count()}")
```

### Output
```
Deleted book: Nineteen Eighty-Four
Remaining books: <QuerySet []>
Total books count: 0
```

## Summary

All CRUD operations were successfully performed:
- **Create**: Added a new Book instance to the database
- **Retrieve**: Fetched and displayed book details
- **Update**: Modified the book title and saved changes
- **Delete**: Removed the book from the database and confirmed deletion

These operations demonstrate Django ORM's capabilities for database interaction through Python code.