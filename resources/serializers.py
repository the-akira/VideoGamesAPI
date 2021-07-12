from rest_framework import serializers
from .models import Game, Director, Genre, Platform, Screenshot

class ScreenshotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['id','game','screenshot_1','screenshot_2','screenshot_3','screenshot_4']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre 
        fields = ['id','name']

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director 
        fields = ['id','name','born_country']

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform 
        fields = ['id','name','developer','generation','media','cpu','release_date']

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
            'id',
            'title',
            'description',
            'cover',
            'developer',
            'publisher',
            'director',
            'genre',
            'platform',
            'release_date'
        ]