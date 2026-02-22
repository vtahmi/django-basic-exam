from django.core.exceptions import ValidationError


def validate_skill_title_length(value):
    if len(value) < 3:
        raise ValidationError("Skill title must be at least 3 characters long.")