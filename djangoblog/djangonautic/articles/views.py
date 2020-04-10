from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-date')
    context  = {
        'articles':articles
    }
    return render(request, 'articles/article_list.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article':article
    }
    return render(request, 'articles/article_detail.html', context)
    #return HttpResponse(slug)

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance        = form.save(commit=False) # Commit = False means to wait for a moment but give us the save instance
            instance.author = request.user
            instance.save()
            # save article to db
            return redirect('articles:article-list')
    else:
        form = forms.CreateArticle()
    context = {
        'form':form
    }
    return render(request, 'articles/article_create.html', context)

def article_list_of_author(request, userid):
    #articles = get_object_or_404(Article, userid)
    articles = Article.objects.filter(author=userid).order_by('-date')
    context  = {
        'articles':articles
    }
    print('INSIDE..')
    return render(request, 'articles/user_articles.html', context)

def article_update(request, userid, articleid):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=articleid)
        form    = forms.CreateArticle(request.POST or None, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article-list')
    else:
        article = get_object_or_404(Article, id=articleid)
        form    = forms.CreateArticle(request.GET or None, instance=article)
    context = {
        'form':form,
    }

    return render(request, 'articles/article_update.html', context)

def article_delete(request, articleid, *args, **kwargs):
    article = get_object_or_404(Article, id=articleid)
    context = {}
    if request.method == 'POST':
        if 'confirm delete' in request.POST:
            # if condition checks if POST request is coming from article_delete.html
            # by clicking the Confirm Delete button
            article.delete()
            return redirect('articles:article-list')
        else:
            context = {
                'article': article
            }

    return render(request, 'articles/article_delete.html', context)