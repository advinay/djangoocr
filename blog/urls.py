from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^(?P<slug>.+)$', lire_article, name='blog_lire'),
]
