from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.order_by('-created_at')
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_at = timezone.now()
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)
