from django.contrib import admin
from .models import WeightRecord

@admin.register(WeightRecord)
class WeightRecordAdmin(admin.ModelAdmin):
    list_display = ['weight', 'date_recorded', 'time_created']
    list_filter = ['date_recorded', 'time_created']
    search_fields = ['date_recorded']
    prepopulated_fields = {'slug': ('date_recorded',)}
    date_hierarchy = 'date_recorded'
    ordering = ['date_recorded', 'time_created']

