from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name


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
    title = models.CharField(max_length=50, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist', null=True)
    uploaded_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    file = models.FileField(upload_to='media/', default='song')
    likes = models.ManyToManyField(User, related_name='song_likes', blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='album', null=True)

    class Meta:
        ordering = ['uploaded_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='album_likes', blank=True)
    image = CloudinaryField('album cover', default='image')
    description = models.TextField(default='description')
    
    

    class Meta:
        ordering = ['created_on']

    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title


    




