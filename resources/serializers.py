from rest_framework import serializers
from .models import Game, Director, Genre, Platform

class GenreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Genre 
		fields = ['name']

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Director 
		fields = ['name']

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Platform 
		fields = ['name','developer','generation','media','cpu']

class GameSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="director-detail"
    )

    genre = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="genre-detail"
    )

    platform = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="platform-detail"
    )
    
    class Meta:
    	model = Game
    	fields = [
    		'title',
    		'description',
    		'publisher',
    		'director',
    		'genre',
    		'platform',
    		'release_date'
    	]