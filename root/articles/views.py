from django.shortcuts import render, HttpResponse
from .models import Article
# Create your views here.

def main(request):
    articles = Article.objects.all()
    return render(request, 'articles/main.html', {'articles': articles})

def show(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/ContentArticle.html', {'article':article})

def books(request):
    return HttpResponse('unavailable')