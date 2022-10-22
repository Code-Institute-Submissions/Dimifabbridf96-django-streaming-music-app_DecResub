from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_surname = models.CharField(max_length=50)

    def __str__(self):
        return artist_name + artist_surname

class Album(models.Model):
    album_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name = 'album_artist')
    album_title = models.CharField(max_length=200, unique=True)
    created_on = models.DateField()
    genre = models.ForeignKey(Genre)
    songs = models.ForeignKey(Song)
    album_image = CloudinaryField('image', default='image')

    def __str__(self):
        return album_title


class Genre(models.Model):
    GENRE = (
        ('R','Rock'),
        ('J','Jazz'),
        ('P','Pop'),
        ('H','House'),
        ('B','Blues'),
        ('M','Metal'),

    )
    genre = models.CharField(max_length=1, choices=GENRE)
    other = models.CharField(max_length=20)

    def __str__(self):
        return genre

class Song(models.Model):
    song_title = models.CharField(max_length=50, unique=True)
    song_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name = 'song_artist')
    uploaded_on = models.DateTimeField(auto_now=True)
    song_album = models.ForeignKey(Album, on_delete=models.on_delete.CASCADE, related_name = 'song_album')

    def __str__(self):
        return song_title

    




