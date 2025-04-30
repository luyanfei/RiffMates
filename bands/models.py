from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    def __str__(self):
        return f'Musician {self.id}: {self.first_name} {self.last_name}'
    
class Venue(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'Venue {self.id}: {self.name}'
    
class Room(models.Model):
    name = models.CharField(max_length=50)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    def __str__(self):
        return f'Room {self.id}: {self.name} at {self.venue}'
    
class Band(models.Model):
    name = models.CharField(max_length=50)
    musicians = models.ManyToManyField(Musician)
    def __str__(self):
        return f'Band {self.id}: {self.name}'
    

    
