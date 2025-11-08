from django.db import models

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NONFICTION', 'Non-Fiction'),
        ('EDUCATION', 'Education'),
        ('SCIENCE', 'Science'),
        ('BIO', 'Biography'),
        ('TECH', 'Technology'),
    ]
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    publication_year = models.DateField(default=2004)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default='FICTION')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title
