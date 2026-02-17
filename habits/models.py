from django.db import models

from skills.models import Skill


class Habit(models.Model):
    name = models.CharField(max_length=100)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='habits')
    frequency = models.PositiveSmallIntegerField(help_text='Number of times per week')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
