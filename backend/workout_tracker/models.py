from django.db import models

# Create your models here.

class Program(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_type = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    resets = models.IntegerField(default=0)

class Workout(models.Model):
    wo_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField()

class Excersie(models.Model):
    ex_id = models.AutoField(primary_key=True)
    wo_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)