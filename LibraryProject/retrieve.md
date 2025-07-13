# Retrieve Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"Book ID: {book.id}")
```

## Expected Output
```
Title: 1984
Author: George Orwell
Publication Year: 1949
Book ID: 1
```

## Alternative Retrieval Methods
```python
# Retrieve all books
all_books = Book.objects.all()
print(f"All books: {all_books}")

# Retrieve books by author
orwell_books = Book.objects.filter(author="George Orwell")
print(f"Books by George Orwell: {orwell_books}")
```

The retrieve operation successfully fetches the book from the database and displays all its attributes.