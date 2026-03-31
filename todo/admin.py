from django.contrib import admin
from .models import tasks

class tasksAdmin(admin.ModelAdmin):
    list_display = ('task','iscompleted')
    search_fields=('task',)

admin.site.register(tasks,tasksAdmin)