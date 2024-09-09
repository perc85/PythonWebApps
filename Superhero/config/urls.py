from django.urls import path
from hero.views import HulkView

urlpatterns = [
    path('',        HulkView.as_view()),
]
