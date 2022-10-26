from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_surname = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_surname 


class Genre(models.Model):
    GENRE = (
        ('R', 'Rock'),
        ('J', 'Jazz'),
        ('P', 'Pop'),
        ('H', 'House'),
        ('B', 'Blues'),
        ('M', 'Metal'),

    )
    genre = models.CharField(max_length=1, choices=GENRE)
    other = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.genre


class Song(models.Model):
    song_title = models.CharField(max_length=50, unique=True)
    song_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song_artist')
    uploaded_on = models.DateTimeField(auto_now=True)
    song_file = models.FileField(upload_to='media/', default='song')
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='song_likes', blank=True)

    class Meta:
        ordering = ['uploaded_on']

    def __str__(self):
        return self.song_title
    
    def number_of_likes(self):
        return self.likes.count()


class Album(models.Model):
    album_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='album_artist')
    album_title = models.CharField(max_length=200, unique=True)
    created_on = models.DateField()
    album_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='album_likes', blank=True)
    album_image = CloudinaryField('album cover', default='image')

    class Meta:
        ordering = ['created_on']

    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.album_title


    




