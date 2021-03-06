from django.db import models
from django.contrib.auth.models import User

class GameCategory(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Game(models.Model):
    owner = models.ForeignKey(User,
                              related_name='games',
                              on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True , default='')
    release_date = models.DateTimeField()
    played = models.BooleanField(default=False)
    
    game_category = models.ForeignKey(GameCategory,
                                      related_name='games',
                                      on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Player(models.Model):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              default='M')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Score(models.Model):
    score = models.IntegerField()
    score_date = models.DateTimeField()

    player = models.ForeignKey(Player,
                               related_name='scores',
                               on_delete=models.CASCADE)
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE)

    class Meta:
        ordering = ('-score',)
