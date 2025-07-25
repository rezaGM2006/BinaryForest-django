from django.urls import path
from . import views

app_name = 'chatroom'

urlpatterns = [
    path('', views.main, name = 'main'),
    path('chat/', views.chat, name = 'ChatCity'),

]