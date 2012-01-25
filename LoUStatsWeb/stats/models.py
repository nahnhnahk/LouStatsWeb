from django.db import models

# Create your models here.
class PlayerScore(models.Model):    
    index = models.IntegerField()
    points = models.IntegerField()
    timestamp = models.DateTimeField(auto_now = True)
        
#    def __repr__(self):
#        return "<PlayerScoreEntry(%s, %s, %s)>" % \
#            (self.index, self.points, self.timestamp)