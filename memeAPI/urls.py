from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import MemeViewSet
from dashboard.models import Meme

router = SimpleRouter(trailing_slash=False)
router.register(r'memes', MemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',  namespace='rest_framework')),
]