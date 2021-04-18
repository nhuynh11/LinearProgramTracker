from rest_framework import serializers
from .models import Program, Workout, Exercise

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'program_type', 'start_date', 'end_date', 'resets')

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'program', 'date', 'theme')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'workout', 'name', 'sets', 'reps')
