from django import forms
from django.contrib.auth import authenticate
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.auth.hashers import make_password
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


class SearchForm(forms.Form):
    name = forms.CharField(label='Tytuł książki', max_length=128)
