"""
@author: Przemyslaw Bieganski, bieg4n@gmail.com
"""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

@python_2_unicode_compatible  # WOW! naprawde istotne
class MusicEvents(models.Model):
    '''
    Main table for music events.
    '''
    artist = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50)
    event_date = models.CharField(max_length=25)
    lineup = models.TextField()
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return '{} at {}'.format(self.title, self.place)
