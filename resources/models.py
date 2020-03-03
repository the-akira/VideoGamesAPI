from django.db import models

class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Genre(DateTimeModel):
    """Model representing a game genre"""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Platform(DateTimeModel):
    """Model representing a game platform"""
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    generation = models.CharField(max_length=50)
    media = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Director(DateTimeModel):
    """Model representing a game director"""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Game(DateTimeModel):
    """Game model"""
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
    publisher = models.CharField(max_length=100)
    director = models.ManyToManyField(Director, help_text='Select a director for this game')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this game')
    platform = models.ManyToManyField(Platform, help_text='Select a platform for this game')
    release_date = models.DateField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title