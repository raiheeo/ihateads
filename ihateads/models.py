from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator



class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KZ')
    STATUS_CHOICES = [
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')
    countries = models.ManyToManyField(Country, blank=True, related_name='users')

    def __str__(self):
        return self.username

class Director(models.Model):
    director_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    director_image = models.ImageField(upload_to='directors/', blank=True, null=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    actor_image = models.ImageField(upload_to='actors/', blank=True, null=True)

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name



class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    countries = models.ManyToManyField(Country, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    TYPES_CHOICES = [
        ('144', '144p'),
        ('360', '360p'),
        ('480', '480p'),
        ('720', '720p'),
        ('1080', '1080p'),
    ]
    types = models.CharField(max_length=10, choices=TYPES_CHOICES)
    movie_time = models.PositiveIntegerField()
    description = models.TextField()
    movie_trailer = models.URLField(blank=True, null=True)
    movie_image = models.ImageField(upload_to='movies/', blank=True, null=True)
    STATUS_CHOICES = [
        ('pro', 'Pro'),
        ('simple', 'Simple'),
    ]
    status_movie = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.movie_name


class MovieLanguage(models.Model):
    language = models.CharField(max_length=50)
    video = models.FileField(upload_to='movie_languages/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return f"{self.movie.movie_name} ({self.language})"


class Moment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moments')
    movie_moment = models.ImageField(upload_to='movie_moments/')

    def __str__(self):
        return f"Moment from {self.movie.movie_name}"


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveIntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.movie_name} ({self.stars} stars)"


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Favorites"


class FavoriteMovie(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f"{self.favorite.user.username} - {self.movie.movie_name}"


class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='history')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='history')
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} watched {self.movie.movie_name}"
