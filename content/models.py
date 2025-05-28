from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from bands.models import Band, Musician

class MusicianBandChoice(models.TextChoices):
    MUSICIAN = 'M'
    BAND = 'B'

class SeekingAd(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    seeking = models.CharField(max_length=1, choices=MusicianBandChoice.choices)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True, blank=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.owner.username} is seeking {self.seeking}'

    def clean(self):
        if self.seeking == MusicianBandChoice.MUSICIAN:
            if self.band is None:
                raise ValidationError('Band field required when seeking a musician')
            if self.musician is not None:
                raise ValidationError('Musician field should be empty when seeking a musician')
        else:
            if self.musician is None:
                raise ValidationError('Musician field required when seeking a band')
            if self.band is not None:
                raise ValidationError('Band field should be empty when seeking a band')
        super().clean()
  
