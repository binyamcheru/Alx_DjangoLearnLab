from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom admin configuration for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns in list view
    list_filter = ('author', 'publication_year')            # Add filtering by author and year
    search_fields = ('title', 'author')                     # Enable search by title and author


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth']

admin.site.register(CustomUser, CustomUserAdmin)
