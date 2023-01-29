from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from filmes.views import FilmeViewSet

router = routers.DefaultRouter()
router.register('filmes', FilmeViewSet, basename='filmes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
