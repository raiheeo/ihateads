from .models import *
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['age', 'phone_number', 'status', 'countries']  

class CountrySerializer(serializers.ModelSerializer):  
    class Meta:
        model = Country
        fields = ['country_name']

class DirectorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age', 'director_name', 'director_image']

class ActorSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_name', 'actor_image']

class GenreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genre
        fields = ['genre_name']

class MovieSerializer(serializers.ModelSerializer): 
    countries = CountrySerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            'movie_name', 'movie_image', 'year', 'description', 'countries', 
            'directors', 'actors', 'genres', 'types', 'movie_time', 'status_movie'
        ]

class MovieLanguageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MovieLanguage
        fields = ['language', 'video', 'movie']

class MomentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Moment
        fields = ['movie_moment', 'movie']

class RatingSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Rating
        fields = ['user', 'movie',  'stars', 'parent', 'text', 'created_date']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'created_date']

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['favorite', 'movie']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']