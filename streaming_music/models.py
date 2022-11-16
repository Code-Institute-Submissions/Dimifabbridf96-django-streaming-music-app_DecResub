from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=50, unique=True)
    artist_name = models.CharField(max_length=40)
    artist_surname = models.CharField(max_length=30)
    uploaded_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    file = models.FileField(upload_to='media/', default='song')
    likes = models.ManyToManyField(User, related_name='song_likes', blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='album')

    class Meta:
        ordering = ['uploaded_on']
        unique_together = ('artist_name', 'artist_surname')

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


class Album(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateField(auto_now=True)
    genre = models.CharField(max_length=20)
    likes = models.ManyToManyField(User, related_name='album_likes', blank=True)
    image = models.ImageField(upload_to='django-image/', default='https://streaming-music-app.s3.eu-west-1.amazonaws.com/static/image/spotiflix.jpg' )
    description = models.TextField(default='description')
    
    

    class Meta:
        ordering = ['created_on']

    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title


    




