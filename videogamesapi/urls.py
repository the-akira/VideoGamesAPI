from django.contrib import admin
from django.urls import include, path
from videogamesapi import views
from resources import views as resources_views
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework import routers

schema_view = get_schema_view(
    title='Video Games API',
    version='0.1', 
    renderer_classes=[JSONOpenAPIRenderer]
)

router = routers.DefaultRouter()

router.register(r'games', resources_views.GameViewSet)
router.register(r'platforms', resources_views.PlatformViewSet)
router.register(r'screenshots', resources_views.ScreenshotViewSet)
router.register(r'directors', resources_views.DirectorViewSet)
router.register(r'genres', resources_views.GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('documentation/', views.documentation, name='documentation'),
    path('schema', schema_view),
]