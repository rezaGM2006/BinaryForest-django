from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name = 'main'),
    path('about-us/', views.about_us, name = 'about-us')
]