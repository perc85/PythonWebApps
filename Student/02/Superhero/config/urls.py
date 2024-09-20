from django.urls import path
from hero.views import HulkView, IndexView, CaptainView, WonderView, PantherView

urlpatterns = [
    path('',        IndexView.as_view()),
    path('hulk',        HulkView.as_view()),
    path('captain',        CaptainView.as_view()),
    path('wonder',        WonderView.as_view()),
    path('panther',        PantherView.as_view()),
]

