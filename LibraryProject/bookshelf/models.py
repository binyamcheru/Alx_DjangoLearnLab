from django.db import models

class Book(models.Model):
    """
    A model representing a book in the library.
    
    Attributes:
        title: The title of the book (max 200 characters)
        author: The author of the book (max 100 characters)
        publication_year: The year the book was published
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'