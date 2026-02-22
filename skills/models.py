from django.db import models

from profiles.models import Profile
from skills.validators import validate_skill_title_length


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100, validators=[validate_skill_title_length])
    description = models.TextField()
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    categories = models.ManyToManyField(Category, related_name='skills')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
