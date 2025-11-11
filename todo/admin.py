from django.contrib import admin
from .models import Task   # ✅ same model name as defined in models.py

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')

admin.site.register(Task, TaskAdmin)
