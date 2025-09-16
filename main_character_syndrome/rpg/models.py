from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    game = models.CharField(max_length=100)
    class_job = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    abilities = models.ManyToManyField('Ability', blank=True)

    def __str__(self):
        return f'{self.name} from {self.game}'


class Ability(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25)
    element = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'{self.name}'
    
