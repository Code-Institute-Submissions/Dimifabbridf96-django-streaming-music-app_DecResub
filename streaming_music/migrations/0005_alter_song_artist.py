# Generated by Django 3.2.16 on 2022-11-17 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_music', '0004_alter_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='streaming_music.artist'),
        ),
    ]