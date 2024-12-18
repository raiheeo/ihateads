# Generated by Django 5.1.4 on 2024-12-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihateads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors_de',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors_en',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors_ru',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='countries_de',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='countries_en',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='countries_ru',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors_de',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors_en',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors_ru',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres_de',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres_en',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres_ru',
            field=models.ManyToManyField(null=True, related_name='movies', to='ihateads.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
