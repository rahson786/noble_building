from django.contrib import admin
from .models import Project, Tag, People

# Register your models here.

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(People)