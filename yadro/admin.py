from django.contrib import admin

from .models import DataRecord


@admin.register(DataRecord)
class DataRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'priority', 'is_active', 'created_at')
    list_filter = ('category', 'status', 'priority', 'is_active')
    search_fields = ('title', 'category', 'status', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
