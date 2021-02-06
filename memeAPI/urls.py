from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import MemeViewSet
from dashboard.models import Meme

router = DefaultRouter()
router.register(r'memes', MemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',  namespace='rest_framework')),
    # path('', views.TestView.as_view(), name='test'),
]

# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from memeAPI import views

# urlpatterns = [
#     path('memes/', views.MemeListView.as_view()),
#     path('memes/<int:pk>/', views.MemeListView.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)