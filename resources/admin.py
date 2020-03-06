from django.contrib import admin
from .models import Game, Director, Genre, Platform, Screenshot

classes = [Director, Genre, Screenshot]

class GameAdmin(admin.ModelAdmin):
	list_display = (
			'id',
			'title',
    		'description',
            'cover',
            'developer',
    		'publisher',
    		'release_date')
	list_display_links = ('id','title')
	search_fields = ('title',)
	list_per_page = 20

class PlatformAdmin(admin.ModelAdmin):
	list_display = (
			'id',
			'name',
    		'developer',
            'generation',
            'media',
    		'cpu',
    		'release_date')
	list_display_links = ('id','name')
	search_fields = ('name',)
	list_per_page = 20

admin.site.register(Game, GameAdmin)
admin.site.register(Platform, PlatformAdmin)
for c in classes:
	admin.site.register(c)