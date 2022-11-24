from django.contrib import admin
from admissions.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','fathername','classname']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','experience','contact']

# Register your models here.

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
