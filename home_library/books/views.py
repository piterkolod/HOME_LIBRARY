from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.contrib.auth import authenticate, login
from django.views.generic.edit import (
    FormView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import (
    Author,
    Book,
    Publisher,
    Reader
)


from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse, reverse_lazy

# Create your views here.

class CatalogView(View):
    def get(self, request):
        books = Book.objects.all()
        ctx = {"books": books}
        return render(request, 'catalog.html', ctx)


class BookView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        ctx = {"book": book}
        return render(request, 'books/book.html', ctx)


class AddBookView(CreateView):
    model = Book
    fields = ['title', 'author', 'type', 'genre', 'publisher', 'description', 'year', 'logo']


#LoginRequiredMixin
class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('homepage')


class UpdateBookView(UpdateView):
    model = Book
    fields = '__all__'


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('homepage'))