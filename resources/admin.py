from django.contrib import admin
from .models import Game, Director, Genre, Platform

classes = [Game, Director, Genre, Platform]

for c in classes:
	admin.site.register(c)