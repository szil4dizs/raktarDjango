from django.contrib import admin
from .models import Store, Invoice, Machine

# Register your models here.
admin.site.register(Store)
#admin.site.register(Invoice)
# admin.site.register(Machine)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'purchase_date', 'store')
    search_fields = ('invoice_number', 'store__name')

admin.site.register(Invoice, InvoiceAdmin)

class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'serial_number', 'status')
    list_filter = ('status', 'type')
    search_fields = ('name', 'type', 'serial_number')

    #form mezők csoportosítása
    fieldsets = (
        ("Alapadatok", {'fields': ('name', 'type', 'manufacturer_code', 'lot_number', 'serial_number')}),
        ("Beszerzés", {'fields': ('invoice', 'price')}),
        ("Állapot", {'fields': ('status', 'parent')}),
        ("További információ", {'fields': ('description',)}),
    )

admin.site.register(Machine, MachineAdmin)
