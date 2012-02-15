from django.contrib import admin
from models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date_created', 'date_modified']
    pass

admin.site.register(Resource, ResourceAdmin)