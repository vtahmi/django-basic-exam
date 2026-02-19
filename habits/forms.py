from django import forms

from habits.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'skill', 'frequency']
