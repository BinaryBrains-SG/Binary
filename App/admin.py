from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Doubt)
admin.site.register(Video)
admin.site.register(Student)