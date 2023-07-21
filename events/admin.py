from django.contrib import admin

from .models import Notice, Events

# Register your models here.
admin.site.register(Notice)
admin.site.register(Events)