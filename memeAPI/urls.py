from django.urls import path
from memeAPI import views
from dashboard.models import Meme
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('memes', views.meme_list),
    path('memes/<int:pk>', views.meme_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)