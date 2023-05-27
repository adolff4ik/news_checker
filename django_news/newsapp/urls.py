from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home_url'),
    path('headlines', headlines, name='heaflines_url'),
    path('everything', everything, name='everything_url'),
    path('articles', ShowArticles.as_view(), name='articles_url'),
    path('headlines/results', HeadlineSerch.as_view(), name='results_headlines_url'),
    path('everything/results', EverythingSearch.as_view(), name='results_everything_url'),
    #path('articles/<int:artcl_id>', show_artcl, name='artcl_url'),
]
