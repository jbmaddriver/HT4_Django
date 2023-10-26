from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_level = models.CharField(max_length=20)
    date_start = models.DateField()
    duration = models.CharField(max_length=20)
    number_of_students = models.IntegerField()
    average_mark = models.FloatField()

    def __str__(self):
        return (f"{self.group_name} {self.group_level} {self.date_start} {self.duration} "
                f"{self.number_of_students} {self.average_mark}")
