from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Game, Director, Genre, Platform, Screenshot
from .serializers import (
	ScreenshotSerializer,
	GenreSerializer,
	DirectorSerializer,
	PlatformSerializer,
	GameSerializer
)

class ScreenshotViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Screenshot.objects.order_by('id')
	serializer_class = ScreenshotSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Genre.objects.order_by('id')
	serializer_class = GenreSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Director.objects.order_by('id')
	serializer_class = DirectorSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Platform.objects.order_by('id')
	serializer_class = PlatformSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class GameViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Game.objects.order_by('id')
	serializer_class = GameSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['title']