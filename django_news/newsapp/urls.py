from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home_url'),
    path('results', search, name='results')
]
