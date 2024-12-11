from django.urls import path
from .views import *
from django.conf import settings
from .models import *
from .serializers import *


urlpatterns = [
    path('', MovieViewSet.as_view({'get': 'list',
                                     'post': 'create'}), name='movie_list'),

    path('<int:pk>/',  MovieViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail')
]

