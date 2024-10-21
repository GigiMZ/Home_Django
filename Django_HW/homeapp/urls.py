from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('create_article/', views.create_article, name="crt_articles")
]