from django.db import models
from django.utils import timezone

# Create your models here.

class Program(models.Model):
    program_type = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    resets = models.IntegerField(default=0)

    def __str__(self):
        return self.program_type + " Program " + str(self.id)

    def program_length(self):
        if self.end_date:
            return self.end_date - self.start_date
        else:
            return timezone.now() - self.start_date

class Workout(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField()
    theme = models.CharField(max_length=200)

    def __str__(self):
        return self.theme + " Workout " + str(self.id)

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.id)