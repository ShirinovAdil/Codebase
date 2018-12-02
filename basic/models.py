from django.db import models


class Course(models.Model):

    course_name = models.CharField(max_length=140)
    course_price = models.IntegerField()
    course_date_1 = models.DateTimeField()
    course_date_2 = models.DateTimeField()
    places = models.IntegerField(default=10)
    empty_places = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name
