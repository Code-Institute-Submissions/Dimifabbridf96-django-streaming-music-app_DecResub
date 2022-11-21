from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

GENRE = [
    ('Rock', 'Rock'),
    ('Jazz', 'Jazz'),
    ('Pop', 'Pop'),
    ('House', 'House'),
    ('Blues', 'Blues'),
    ('Metal', 'Metal'),
    ('Other', 'Other')
]

class Song(models.Model):
    title = models.CharField(max_length=50, unique=True)
    first_name_artist = models.CharField(max_length=50)
    last_name_artist = models.CharField(max_length=50)
    uploaded_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    file = models.FileField(upload_to='media/', default='song')
    likes = models.ManyToManyField(User, related_name='song_likes', blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='album', default=None)

    class Meta:
        ordering = ['uploaded_on']

    def __str__(self):
        return self.title
    

class Album(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateField(auto_now=True)
    genre = models.CharField(max_length=5, choices=GENRE, default=None)
    likes = models.ManyToManyField(User, related_name='album_likes', blank=True)
    image = models.ImageField(upload_to='django-image/', default='default')
    description = models.TextField(default='description')
    
    class Meta:
        ordering = ['created_on']

    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title

    




