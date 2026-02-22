from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
