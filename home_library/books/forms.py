from django import forms
from django.contrib.auth import authenticate
from django.db.models import Value
from django.db.models.functions import Concat
# from .validators import valid_range
from books.models import (
    Author,
    Book,
    Publisher,
    Reader
)


class AddBookForm(forms.Form):

    class Meta:
        model = Book
        fields = '__all__'