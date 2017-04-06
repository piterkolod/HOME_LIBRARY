from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    lat_name = models.CharField(max_length=64)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.lat_name)


class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    BOOK_TYPE = (
        (1, 'paper book'),
        (2, 'ebook'),
        (3, 'audiobook')
    )
    type = models.IntegerField(choices=BOOK_TYPE, default=1)
    GENRES = (
        (1, 'crime'),
        (2, 'fantasy'),
        (3, 'sci-fi'),
        (4, 'romance'),
        (5, 'popular science'),
        (6, 'thriller'),
        (7, 'adventure'),
        (8, 'for children'),
        (9, 'poem'),
        (10, 'religion'),
        (11, 'travel')
    )
    genre = models.IntegerField(choices=GENRES, default=1)
    publisher = models.ForeignKey(Publisher, related_name='publisher')
    description = models.TextField(null=True)
    year = models.IntegerField(default=None)
    logo = models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return '{}{}'.format(self.title, self.author)

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.id})


class Reader(models.Model):
    user = models.OneToOneField(User, null=True, default=None)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=70,blank=True)
    password = models.CharField(max_length=256)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.username
