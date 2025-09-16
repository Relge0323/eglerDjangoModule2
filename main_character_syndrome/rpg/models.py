from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    game = models.CharField(max_length=100)
    class_job = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    abilities = models.ManyToManyField('Ability', blank=True)
    quests = models.ManyToManyField('Quest', blank=True)

    def __str__(self):
        return f'{self.name} from {self.game}'


class Ability(models.Model):
    name = models.CharField(max_length=100)
    ability_type = models.CharField(max_length=25)
    element = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'{self.name}'
    

class Quest(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    reward = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} is a {self.difficulty} quest'
    

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    slot_type = models.CharField(max_length=50)
    
    characters = models.ManyToManyField('Character', blank=True, related_name='equipment')

    def __str__(self):
        return f'{self.name}'