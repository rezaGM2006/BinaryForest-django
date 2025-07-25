from django.db import models

# Create your models here.



class Chat(models.Model):
    username = models.CharField(max_length=300)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    

