from django.contrib import admin
from .models import tasks

class tasksAdmin(admin.ModelAdmin):
    list_display = ('task','iscompleted')

admin.site.register(tasks,tasksAdmin)