from django.urls import path
from hero.views import HulkView, IndexView, CaptainView, WonderView, PantherView

urlpatterns = [
    path('',        IndexView.as_view()),
    path('',        HulkView.as_view()),
    path('',        CaptainView.as_view()),
    path('',        WonderView.as_view()),
    path('',        PantherView.as_view()),
]
