from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


# Create your views here

def index(request):
    return render(request, 'theme.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('article_list')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})


@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article created successfully!")
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.author:
        return redirect('article_detail', pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article updated successfully!")
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        article.delete()
        messages.success(request, "Article deleted successfully!")
    return redirect('article_list')

