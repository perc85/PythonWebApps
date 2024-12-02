from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('profile/', views.investigator_profile, name='investigator_profile'),
    path('investigators/', views.investigator_list, name='investigator_list'),
    path('investigators/<int:pk>/', views.investigator_detail, name='investigator_detail'),
    path('redirect_after_login/', views.redirect_after_login, name='redirect_after_login'),
    path('investigators/<int:pk>/delete/', views.investigator_delete, name='investigator_delete'),
    path('superheroes/', views.superhero_list, name='superhero_list'),
    path('superheroes/<int:pk>/', views.superhero_detail, name='superhero_detail'),
    path('superheroes/new/', views.superhero_create, name='superhero_create'),
    path('superheroes/<int:pk>/edit/', views.superhero_update, name='superhero_update'),
    path('superheroes/<int:pk>/delete/', views.superhero_delete, name='superhero_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]