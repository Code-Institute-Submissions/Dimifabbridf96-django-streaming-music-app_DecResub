from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

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
    file = models.FileField(upload_to='media/', default='song')
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='album', default=None)

    class Meta:
        ordering = ['uploaded_on']

    def __str__(self):
        """
        return a string with title value
        """
        return self.title
    

class Album(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateField(auto_now=True)
    genre = models.CharField(max_length=5, choices=GENRE, default=None)
    likes = models.ManyToManyField(User, related_name='album_likes', blank=True)
    image = models.ImageField(upload_to='django-image/', default='default')
    description = models.TextField(default='description')
    
    class Meta:
        ordering = ['created_on']

    def number_of_likes(self):
        """
        return a count of the likes
        """
        return self.likes.count()
    
    def __str__(self):
        """
        return a string with title value
        """
        return self.title


class Comment(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        return a string with body value and name value
        """
        return f"Comment {self.body} by {self.name}"
    




