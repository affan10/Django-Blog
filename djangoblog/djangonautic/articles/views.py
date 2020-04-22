from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from django.http import HttpResponse

from .models import Article
from . import forms


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


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # Commit = False means to wait for a moment but give us the save instance
            instance        = form.save(commit=False)
            instance.author = request.user
            # Appending author to slug so that different users can post articles with the same names
            instance.slug = instance.author.username + '-' + form.cleaned_data['slug']
            instance.save()

            return redirect('articles:article-list')
    else:
        form = forms.CreateArticle()
    context = {
        'form':form
    }
    return render(request, 'articles/article_create.html', context)


def article_list_of_author(request, userid):
    articles = Article.objects.filter(author=userid).order_by('-date')
    context  = {
        'articles':articles
    }
    return render(request, 'articles/user_articles.html', context)


def article_update(request, userid, articleid):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=articleid)
        form    = forms.CreateArticle(request.POST or None, request.FILES, instance=article)
        if form.is_valid():
            instance      = form.save(commit=False)
            instance.slug = instance.author.username + '-' + form.cleaned_data['slug']
            instance.save()
            return redirect('articles:article-list')
    else:
        article = get_object_or_404(Article, id=articleid)
        form    = forms.CreateArticle(request.GET or None, instance=article)
    context = {
        'form':form,
    }

    return render(request, 'articles/article_update.html', context)


def article_delete(request, articleid):
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


class SearchView(ListView):
    model         = Article
    template_name = 'articles/search_results.html'

    def get_queryset(self):
        articles = []
        query    = self.request.GET['q']
        query    = query.split(' ')
        for word in query:
            filtered_articles = Article.objects.filter(
                Q(title__icontains=word) | Q(body__icontains=word) |
                Q(author__username__icontains=word) | Q(thumb__icontains=word)
            ).order_by('-date')

            # For removing duplicate articles fetched by the above filters
            for article in filtered_articles:
                if article not in articles:
                    articles.append(article)

        return articles
