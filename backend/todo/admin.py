from django.contrib import admin
from .models import Todo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register the model here,
admin.site.register(Todo, ToDoAdmin)