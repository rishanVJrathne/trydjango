from django.shortcuts import render
from .models import Article

def article_list_view(request):

    articles_queryset = Article.objects.all()
    context = { "articles": articles_queryset }

    return render(request, "articles/list.html", context)


def article_detail_view(request, id=None):

    article = None
    if id is not None:
        article = Article.objects.get(id = id)
    context = {"article": article}
    return render( request, "articles/detail.html", context)
    

