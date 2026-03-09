from django import forms

from habits.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'frequency', 'skills']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter habit name'
            }),
            'frequency': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Times per week'
            }),
            'skills': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'Habit Name',
            'frequency': 'Weekly Frequency',
            'skills': 'Associated Skills',
        }
        help_texts = {
            'frequency': '(1-7 times)',
            'skills': 'Select one or more skills',
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


class HabitEditForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'frequency', 'skills']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.NumberInput(attrs={'class': 'form-control'}),
            'skills': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'Habit Name',
            'frequency': 'Weekly Frequency',
            'skills': 'Associated Skills',
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
