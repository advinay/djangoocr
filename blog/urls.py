from django.conf.urls import url, include
from django.views.generic import ListView

from blog.views import *
from .models import Article


urlpatterns = [
    url(r'^$',ListeArticles.as_view(),name="accueil"),
    # url(r'^(?P<slug>.+)$', lire_article, name="blog_lire"),
    url(r'^categorie/(\d+)$', ListeArticles.as_view(), name='blog_categorie'),
    url(r'^article/(?P<pk>\d+)$', LireArticle.as_view(), name='blog_lire'),
    url(r'^test/',test,name="test"),
]
