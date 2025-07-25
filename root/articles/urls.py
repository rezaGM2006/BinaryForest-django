from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.main, name = 'main'),
    path('show/<int:article_id>/', views.show, name = 'show-article'),
    path('books/', views.books, name = 'books')

]