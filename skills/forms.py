from django import forms

from skills.models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['owner', 'created_at']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter skill title'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe this skill...'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Skill Title',
            'description': 'Description',
            'categories': 'Categories',
            'image': 'Skill Image',
        }

        help_texts = {
            'categories': 'Hold Ctrl to select multiple categories.',
        }

        error_messages = {
            'title': {
                'required': 'Please enter a skill title.',
                'max_length': 'Title is too long.',
            },
        }