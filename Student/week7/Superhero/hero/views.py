from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Superhero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'hero/index.html')

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'hero/superhero_list.html'
    context_object_name = 'superheroes'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Superhero.objects.filter(Q(public=True) | Q(user=self.request.user))
        else:
            return Superhero.objects.filter(public=True)

class SuperheroDetailView(DetailView):
    model = Superhero
    template_name = 'hero/superhero_detail.html'

class SuperheroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero/superhero_form.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    success_url = reverse_lazy('superhero_list')
    extra_context = {'title': 'Add New Superhero'}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SuperheroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero/superhero_form.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    success_url = reverse_lazy('superhero_list')
    extra_context = {'title': 'Edit Superhero'}

    def get_queryset(self):
        return Superhero.objects.filter(user=self.request.user)
    

class SuperheroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/superhero_confirm_delete.html'
    success_url = reverse_lazy('superhero_list')

    def get_queryset(self):
        return Superhero.objects.filter(user=self.request.user)

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


