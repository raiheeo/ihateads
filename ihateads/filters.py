from django_filters import FilterSet
from .models import *


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['gt', 'lt'],
            'types': ['gt', 'lt'],
            'genres': ['exact'],
            'status_movie': ['exact'],
            'countries': ['exact']
        }

