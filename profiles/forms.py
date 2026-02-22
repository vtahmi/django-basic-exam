from django import forms

from profiles.models import Profile


class ProfileDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

        }
        labels = {
            'bio': 'About Me',
            'image': 'Profile Picture',
        }

        help_texts = {
            'bio': 'Write a short description about yourself.',
            'image': 'Upload a profile picture (optional).',
        }

        error_messages = {
            'name': {
                'required': 'Please enter your name.',
                'max_length': 'Name cannot exceed 100 characters.',
            },
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long.')
        return name
