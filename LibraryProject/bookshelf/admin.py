from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    
    Customizes the admin interface to:
    - Display title, author, and publication_year in list view
    - Enable search by title and author
    - Add filtering by publication year
    """
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
    list_per_page = 20
    ordering = ('title',)