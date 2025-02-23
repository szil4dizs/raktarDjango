from django.contrib import admin
from .models import Store, Invoice, Machine

# Register your models here.
admin.site.register(Store)
admin.site.register(Invoice)
# admin.site.register(Machine)

class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'serial_number', 'status')
    list_filter = ('status', 'type')
    search_fields = ('name', 'type', 'serial_number')

admin.site.register(Machine, MachineAdmin)
