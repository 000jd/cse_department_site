from django.contrib import admin
from .models import Users, Student, Alumni, Staff

# Register your models here.
admin.site.register(Users)
admin.site.register(Student)
admin.site.register(Alumni)
admin.site.register(Staff)