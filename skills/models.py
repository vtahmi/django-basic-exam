from django.db import models

from profiles.models import Profile
from skills.validators import validate_skill_title_length


class CategoryChoices(models.TextChoices):
    MENTAL = 'mental', 'Mental'
    PHYSICAL = 'physical', 'Physical'
    CREATIVE = 'creative', 'Creative'
    TECHNICAL = 'technical', 'Technical'
    SOCIAL = 'social', 'Social'

class Skill(models.Model):
    title = models.CharField(max_length=100, validators=[validate_skill_title_length])
    description = models.TextField()
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    category = models.CharField(max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.MENTAL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
