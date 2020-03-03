from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from videogamesapi import views
from resources import views as resources_views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'genres', resources_views.GenreViewSet)
router.register(r'directors', resources_views.DirectorViewSet)
router.register(r'platforms', resources_views.PlatformViewSet)
router.register(r'games', resources_views.GameViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index, name='index')
]