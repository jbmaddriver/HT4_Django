from django.db import models

# Generate 1 user.


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"
