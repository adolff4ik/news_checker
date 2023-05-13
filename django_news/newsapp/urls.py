from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home_url'),
    path('headlines', headlines, name='heaflines_url'),
    path('everything', everything, name='everything_url'),
    path('articles', articles, name='articles_url'),
    path('headlines/results', headlines_search, name='results_headlines_url'),
    path('everything/results', everything_search, name='results_everything_url'),
    path('articles/<int:artcl_id>', show_artcl, name='artcl_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
