from django.shortcuts import render, redirect
from .models import Article
from .forms import Articleform

def articles(request):
    articleform = Articleform()
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles.html', context=context)

def create_article(request):
    articleform = Articleform()

    if request.method == "GET":
        articleform = Articleform(request.GET)
        print(articleform.is_valid())
        if articleform.is_valid():
            articleform.save()
            return redirect('articles')
    context = {"form": articleform}
    return render(request, 'create_article.html', context=context)