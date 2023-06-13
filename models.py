from django.utils import timezone
from django.db import models


class Exercise(models.Model):
    date = models.DateField(default=timezone.now)
    exercise = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return self.exercise
