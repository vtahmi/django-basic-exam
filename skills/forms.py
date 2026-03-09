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
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Skill Title',
            'description': 'Description',
            'category': 'Category',
            'image': 'Skill Image',
        }

        error_messages = {
            'title': {
                'required': 'Please enter a skill title.',
                'max_length': 'Title is too long.',
            },
        }
