import markdown

from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Article, AboutContent

# Create your views here.

def index(request):
    articles = Article.objects.filter(is_show=True).order_by('-date')
    context = {
        'articles': articles,
    }
    return render(request, 'main/index.html', context)

def draft(request):
    #articles = Article.objects.order_by('-date')
    articles = Article.objects.filter(is_show=False).order_by('-date')
    context = {
        'articles': articles,
    }
    return render(request, 'main/index.html', context)

def article(request, title):
    try:
        article = Article.objects.get(title=title)
    except Exception as e:
        print(e.with_traceback, e)

    if article is not None:
        return render(request, 'main/article.html', {
            'article':article,
            'date': article.date.strftime("%Y-%m-%d"),
            'content': markdown.markdown(article.content),
            })

def article_id(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Exception as e:
        print(e.with_traceback, e)

    if article is not None:
        return render(request, 'main/article.html', {
            'article':article,
            'date': article.date.strftime("%Y-%m-%d"),
            'content': markdown.markdown(article.content),
            })


def about(request):
    try:
        about_content = AboutContent.objects.get(id=1)
    except Exception as e:
        print(e.with_traceback, e)

    if AboutContent is not None:
        return render(request, 'main/about.html', {
            'content': markdown.markdown(about_content.content),
            })


