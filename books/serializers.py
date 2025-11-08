from rest_framework import serializers
from .models import Book 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'publication_year', 'price', 'rating', 'genre', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']