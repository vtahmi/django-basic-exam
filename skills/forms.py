from django import forms

from skills.models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['owner', 'created_at']
        labels = {
            'title': 'Skill name',
            'description': 'Description',
            'categories': 'Categories',
        }
