from django.db import models

class World(models.Model):
    name = models.CharField(max_length=30)
    host = models.CharField(max_length=50)
    ajax_end_point = models.CharField(max_length=50)

class Player(models.Model):
    world = models.ForeignKey(World)
    index = models.IntegerField()

class PlayerScore(models.Model):    
    player = models.ForeignKey(Player)
    points = models.IntegerField()
    rank = models.IntegerField()
    timestamp = models.DateTimeField(auto_now = True)