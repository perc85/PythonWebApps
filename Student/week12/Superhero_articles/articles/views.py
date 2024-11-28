from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Article, Investigator, Superhero
from .forms import ArticleForm, InvestigatorForm, SuperheroForm
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_investigator(sender, instance, created, **kwargs):
    if created:
        Investigator.objects.create(user=instance, name=f"Investigator {instance.username}")

@login_required
def investigator_profile(request):
    try:
        investigator = Investigator.objects.get(user=request.user)
    except Investigator.DoesNotExist:
        investigator = None

    if request.method == 'POST':
        form = InvestigatorForm(request.POST, instance=investigator)
        if form.is_valid():
            new_investigator = form.save(commit=False)
            new_investigator.user = request.user
            new_investigator.save()
            return redirect('investigator_list')
    else:
        form = InvestigatorForm(instance=investigator)

    if request.GET.get('skip'):
        return redirect('investigator_list')

    return render(request, 'investigator_form.html', {'form': form, 'investigator': investigator})



def investigator_detail(request, pk):
    investigator = get_object_or_404(Investigator, pk=pk)
    articles = Article.objects.filter(author=investigator.user)
    return render(request, 'investigator_detail.html', {
        'investigator': investigator,
        'articles': articles
    })


def investigator_list(request):
    investigators = Investigator.objects.all()
    user_investigator = False

    if request.user.is_authenticated:
        user_investigator = Investigator.objects.filter(user=request.user).exists()

    return render(request, 'investigator_list.html', {
        'investigators': investigators,
        'user_investigator': user_investigator
    })




@login_required
def investigator_delete(request, pk):
    investigator = get_object_or_404(Investigator, pk=pk, user=request.user)

    if request.method == 'POST':
        investigator.delete()
        return redirect('investigator_list')

    return render(request, 'investigator_confirm_delete.html', {'investigator': investigator})


@login_required
def redirect_after_login(request):
    try:
        Investigator.objects.get(user=request.user)
        return redirect('investigator_list')
    except Investigator.DoesNotExist:
        return redirect('investigator_profile')


def superhero_list(request):
    superheroes = Superhero.objects.all()
    return render(request, 'superhero_list.html', {'superheroes': superheroes})


def superhero_detail(request, pk):
    superhero = get_object_or_404(Superhero, pk=pk)
    return render(request, 'superhero_detail.html', {'superhero': superhero})


@login_required
def superhero_create(request):
    if request.method == 'POST':
        form = SuperheroForm(request.POST, request.FILES)
        if form.is_valid():
            superhero = form.save(commit=False)
            superhero.user = request.user
            superhero.save()
            messages.success(request, "Superhero added successfully!")
            return redirect('superhero_list')
    else:
        form = SuperheroForm()
    return render(request, 'superhero_form.html', {'form': form})


@login_required
def superhero_update(request, pk):
    superhero = get_object_or_404(Superhero, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SuperheroForm(request.POST, request.FILES, instance=superhero)
        if form.is_valid():
            form.save()
            messages.success(request, "Superhero updated successfully!")
            return redirect('superhero_detail', pk=superhero.pk)
    else:
        form = SuperheroForm(instance=superhero)
    return render(request, 'superhero_form.html', {'form': form})


@login_required
def superhero_delete(request, pk):
    superhero = get_object_or_404(Superhero, pk=pk, user=request.user)
    if request.method == 'POST':
        superhero.delete()
        messages.success(request, "Superhero deleted successfully!")
        return redirect('superhero_list')
    return render(request, 'superhero_confirm_delete.html', {'superhero': superhero})
