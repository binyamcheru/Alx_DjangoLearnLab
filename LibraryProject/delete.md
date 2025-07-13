# Delete Operation

## Command
```python
from bookshelf.models import Book

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

## Expected Output
```
Deleted book: Nineteen Eighty-Four
Remaining books: <QuerySet []>
Total books count: 0
```

## Alternative Delete Method
```python
# Delete using filter and delete
deleted_count = Book.objects.filter(author="George Orwell").delete()
print(f"Deleted {deleted_count[0]} book(s)")
```

The delete operation successfully removes the book from the database. The confirmation shows that no books remain in the database after the deletion.