from django.urls import path
from . import views

urlpatterns = [
    path('', views.HeroListView.as_view(), name='hero-list'),
    path('hero/<slug:slug>/', views.HeroDetailView.as_view(), name='hero-detail'),
]
