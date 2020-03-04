from django.contrib import admin
from .models import Game, Director, Genre, Platform, Screenshot

classes = [Game, Director, Genre, Platform, Screenshot]

for c in classes:
	admin.site.register(c)