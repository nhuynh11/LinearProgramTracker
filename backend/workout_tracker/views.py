from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ProgramSerializer, WorkoutSerializer, ExerciseSerializer
from .models import Program, Workout, Exercise

# Create your views here.
def index(request):
    return HttpResponse("Yo")

# basic views for now
class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()