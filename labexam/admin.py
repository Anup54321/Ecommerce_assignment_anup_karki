from django.contrib import admin
from .models import *

# Register your models here.
class LabexamAdmin(admin.ModelAdmin):
    list_display = ['exam_date',
                    'exam_name',
                    'exam_description',
                    'total_marks',
                    'pass_marks',
                    'exam_status']
admin.site.register(Labexam, LabexamAdmin)
