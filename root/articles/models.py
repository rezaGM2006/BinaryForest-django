from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)