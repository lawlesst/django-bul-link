from django.contrib import admin
from models import Resource

class ResourceAdmin(admin.ModelAdmin):
    search_fields = ['pk', 'referrer']
    list_display = ['pk', 'referrer', 'date_created', 'date_modified']
    list_filter = ['referrer', 'date_created', 'date_modified']
    pass

admin.site.register(Resource, ResourceAdmin)