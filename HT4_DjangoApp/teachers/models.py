from django.db import models

#validate_comma_separated_integer_list liberies
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_comma_separated_integer_list(value):
    """
    Validator for ensuring that a comma-separated string contains only integers.
    """
    items = value.split(',')
    for item in items:
        try:
            int(item.strip())
        except ValueError:
            raise ValidationError(
                _('Invalid value: %(value)s. All items must be integers.'),
                params={'value': item},
            )

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    science_field = models.CharField(max_length=100)
    science_degree = models.CharField(max_length=20)
    groups_number_id = models.CharField(max_length=20, validators=[validate_comma_separated_integer_list])


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.science_field} {self.science_degree} {self.groups_number_id}'