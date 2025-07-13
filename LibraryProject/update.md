# Update Operation

## Command
```python
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated book: {book}")
print(f"New title: {book.title}")
```

## Expected Output
```
Updated book: Nineteen Eighty-Four by George Orwell (1949)
New title: Nineteen Eighty-Four
```

## Alternative Update Method
```python
# Update using update() method
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")

# Verify the update
updated_book = Book.objects.get(author="George Orwell")
print(f"Updated book: {updated_book}")
```

The update operation successfully modifies the book's title from "1984" to "Nineteen Eighty-Four" and saves the changes to the database.