"""home_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from books.views import (
    AddBookView,
    BookView,
    CatalogView,
    DeleteBookView,
    LogoutView,
    UpdateBookView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catalog', CatalogView.as_view(), name='homepage'),
    url(r'^add_book', AddBookView.as_view(), name='add-book'),
    url(r'^book/(?P<book_id>(\d)+)', BookView.as_view(), name='book'),
    url(r'^update_book/(?P<pk>\d+)', UpdateBookView.as_view(), name='upd-book'),
    url(r'^delete_book/(?P<pk>\d+)', DeleteBookView.as_view(), name='delete-view'),
    url(r'^login/$', auth_views.login, {'template_name': 'books/login.html'}, name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout')
]
