from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'countries', 'directors', 'actors', 'genres', 'description')


