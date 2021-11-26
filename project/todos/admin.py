# Register your models here.
from django.contrib import admin
from .models import *
from .forms import *

class TodoAdmin(admin.ModelAdmin):
    pass
    # form = Todo
    # search_fields = ["user", "created", "updated"]
    # list_display = ["user", "created", "updated"]
    # readonly_fields = [ 'created', 'updated']

# Register your models here.
admin.site.register(Todo, TodoAdmin)
