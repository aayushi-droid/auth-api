from django.db import models

class Sport(models.Model):
    sport_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sport_name


class Ground(models.Model):
    ground_name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='markets', on_delete=models.CASCADE)

    def __str__(self):
        return self.ground_name + ' | ' + self.sport.sport_name
    

class Match(models.Model):
    game_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    sport_name = models.ForeignKey(Sport, related_name='matches', on_delete =models.CASCADE)
    ground_name = models.ForeignKey(Ground, related_name='matches', on_delete =models.CASCADE)    
    
    class Meta:
        ordering = ('start_time',)
        verbose_name_plural = 'Matches'   
    
    def __str__(self):
        return self.game_name
