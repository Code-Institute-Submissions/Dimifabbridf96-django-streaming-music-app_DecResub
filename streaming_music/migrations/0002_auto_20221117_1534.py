# Generated by Django 3.2.16 on 2022-11-17 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('R', 'Rock'), ('J', 'Jazz'), ('P', 'Pop'), ('H', 'House'), ('B', 'Blues'), ('M', 'Metal')], max_length=10)),
                ('other', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='streaming_music.album'),
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist_surname',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='streaming_music.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streaming_music.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='streaming_music.genre'),
        ),
    ]