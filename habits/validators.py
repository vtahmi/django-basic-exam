from django.core.exceptions import ValidationError


def validate_habit_name_length(value):
    if len(value) < 3:
        raise ValidationError("Habit name must be at least 3 characters long.")

def validate_habit_frequency(value):
    if value < 1 or value > 7:
        raise ValidationError("Frequency must be between 1 and 7 times per week.")
