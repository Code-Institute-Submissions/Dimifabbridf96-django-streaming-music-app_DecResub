# Generated by Django 3.2.16 on 2022-11-06 13:42

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import streaming_music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('created_on', models.DateField()),
                ('image', cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='album cover')),
                ('description', models.TextField(default='description')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('R', 'Rock'), ('J', 'Jazz'), ('P', 'Pop'), ('H', 'House'), ('B', 'Blues'), ('M', 'Metal')], max_length=1)),
                ('other', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to=streaming_music.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('file', models.FileField(default='song', upload_to='media/')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='streaming_music.album')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='streaming_music.artist')),
                ('likes', models.ManyToManyField(blank=True, related_name='song_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['uploaded_on'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='streaming_music.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streaming_music.genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='album_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
