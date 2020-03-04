from django.db import models
import uuid

class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Genre(DateTimeModel):
    """Model representing a game genre"""
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        help_text='Unique ID for this particular genre'
        )
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Platform(DateTimeModel):
    """Model representing a game platform"""
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)

    GEN_STATUS = (
        ('1st', 'First Generation'),
        ('2nd', 'Second Generation'),
        ('3rd', 'Third Generation'),
        ('4th', 'Fourth Generation'),
        ('5th', 'Fifth Generation'),
        ('6th', 'Sixth Generation'),
        ('7th', 'Seventh Generation'),
        ('8th', 'Eighth Generation'),
        ('9th', 'Ninth Generation'),
    )

    generation = models.CharField(
        max_length=3,
        choices=GEN_STATUS,
        help_text='Video Game Generation',
    )

    media = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Director(DateTimeModel):
    """Model representing a game director"""
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        help_text='Unique ID for this particular genre'
        )
    name = models.CharField(max_length=200)
    born_country = models.CharField(max_length=150, default="")
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Game(DateTimeModel):
    """Game model"""
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the game')
    cover = models.CharField(max_length=500, default="")
    developer = models.CharField(max_length=150, default="")
    publisher = models.CharField(max_length=150, default="")
    director = models.ManyToManyField(Director, help_text='Select a director for this game')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this game')
    platform = models.ManyToManyField(Platform, help_text='Select a platform for this game')
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Screenshot(DateTimeModel):
    """Model representing screenshots for a given game"""
    game = models.ForeignKey(Game, related_name="game", on_delete=models.CASCADE)
    screenshot_1 = models.CharField(max_length=500)
    screenshot_2 = models.CharField(max_length=500)
    screenshot_3 = models.CharField(max_length=500)
    screenshot_4 = models.CharField(max_length=500)