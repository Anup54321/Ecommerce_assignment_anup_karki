from django.db import models

# Create your models here.
class Labexam(models.Model):
    exam_date = models.DateField()
    exam_name = models.CharField(max_length=1000)
    exam_description = models.TextField()
    total_marks = models.FloatField()
    pass_marks = models.FloatField()
    exam_status = models.BooleanField()
