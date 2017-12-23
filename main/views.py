import markdown

from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Article

# Create your views here.

def index(request):
    context = {
        'latest_question_list': 'sss',
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

def about(request):
    return render(request, 'main/about.html', context)



