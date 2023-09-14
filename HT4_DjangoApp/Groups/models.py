from django.db import models

# Create your models here.

class Groups_list(models.Model):
    group_name = models.CharField(max_length=50)
    group_level = models.CharField(max_length=20)
    date_start = models.DateField()
    duration = models.CharField(max_length=20)
    # duration = models.DurationField()
    number_of_students = models.IntegerField()
    average_mark = models.FloatField()


    def __str__(self):
        return f'{self.group_name} {self.group_level} {self.date_start} {self.duration} {self.number_of_students} {self.average_mark}'