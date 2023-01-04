from django.shortcuts import render
from .models import Article
from .forms import ArticleForm


def article_list_view(request):

    articles_queryset = Article.objects.all()
    context = { "articles": articles_queryset }

    return render(request, "articles/list.html", context)


def article_search_view(request):

    query_param = request.GET

    article_id = query_param.get('query')
    articles_queryset = Article.objects.all()
    context = { "articles": articles_queryset.filter(id=article_id) }

    return render(request, "articles/list.html", context)


def article_detail_view(request, id=None):

    article = None
    if id is not None:
        article = Article.objects.get(id = id)
    context = {"article": article}
    return render( request, "articles/detail.html", context)


def article_create_view(request):
    
    form = ArticleForm(request.POST or None)
    context = {"form": form, "created": False}

    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get("content")
        article = Article.objects.create(title=title, content=content)
        context['created'] = True
        context['article'] = article
    
    return render(request, "articles/create.html", context)

# def article_create_view(request):

#     context ={"created": False}
#     if request.method == "POST":
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         article = Article.objects.create(title=title, content=content)
#         context['article'] = article
#         context['created'] = True
    
#     return render(request, "articles/create.html", context)
