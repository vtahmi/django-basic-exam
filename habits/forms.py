from django import forms

from habits.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'frequency', 'skill']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter habit name'}),
            'frequency': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Times per week'}),
            'skill': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'name': 'Habit Name',
            'frequency': 'Weekly Frequency',
            'skill': 'Associated Skill',
        }
        help_texts = {
            'frequency': '(1-7 times)',
        }
        error_messages = {
            'name': {
                'required': 'Please enter a habit name.',
                'max_length': 'Habit name is too long.',
            },
            'frequency': {
                'required': 'Please specify frequency.',
            },
            'skill': {
                'required': 'Please select a skill.',
            },
        }


class HabitEditForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'frequency']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'frequency': forms.NumberInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'name': 'Habit Name',
            'frequency': 'Weekly Frequency',
        }
        error_messages = {
            'name': {
                'required': 'Please enter a habit name.',
                'max_length': 'Habit name is too long.',
            },
            'frequency': {
                'required': 'Please specify frequency.',
            },
        }
