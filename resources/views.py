from django.shortcuts import render
from rest_framework import viewsets
from .models import Game, Director, Genre, Platform
from .serializers import (
	GenreSerializer,
	DirectorSerializer,
	PlatformSerializer,
	GameSerializer
)

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	search_fields = ('name',)

class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer
	search_fields = ('name',)

class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Platform.objects.all()
	serializer_class = PlatformSerializer
	search_fields = ('name',)

class GameViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	search_fields = ('title',)