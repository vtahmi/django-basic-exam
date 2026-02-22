from django.db import models

from habits.validators import validate_habit_name_length, validate_habit_frequency
from skills.models import Skill


class Habit(models.Model):
    name = models.CharField(max_length=100, validators=[validate_habit_name_length])
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='habits')
    frequency = models.PositiveSmallIntegerField(validators=[validate_habit_frequency])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
