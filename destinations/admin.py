from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'short_description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def short_description(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Description'
