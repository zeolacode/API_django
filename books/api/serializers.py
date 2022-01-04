from django.db.models import fields
from rest_framework import serializers
from books import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'