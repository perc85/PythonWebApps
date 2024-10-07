from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Superhero

# Create your views here.

class HeroListView(ListView):
    model = Superhero
    template_name = 'heroes.html'
    context_object_name = 'heroes'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero.html'
    context_object_name = 'hero'

    def get_queryset(self):
        return Superhero.objects.filter(slug=self.kwargs['slug'])

