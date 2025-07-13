# Create Operation

## Command
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

## Expected Output
```
Created book: 1984 by George Orwell (1949)
```

## Alternative Method
```python
# Alternative way to create a book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book saved: {book}")
```

The create operation successfully adds a new Book instance to the database with the specified title, author, and publication year.