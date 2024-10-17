from django.urls import path
from . import views

urlpatterns = [
    path('', views.SuperheroListView.as_view(), name='superhero_list'),
    path('hero/<int:pk>/', views.SuperheroDetailView.as_view(), name='superhero_detail'),
    path('hero/add/', views.SuperheroCreateView.as_view(), name='superhero_add'),
    path('hero/<int:pk>/edit/', views.SuperheroUpdateView.as_view(), name='superhero_edit'),
    path('hero/<int:pk>/delete/', views.SuperheroDeleteView.as_view(), name='superhero_delete'),
]
