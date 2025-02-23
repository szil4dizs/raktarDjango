from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    purchase_date = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.invoice_number


class Machine(models.Model):
    STATUS = [
        ("A", "Aktív"),
        ("I", "Inaktív"),
        ("H", "Hiány"),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    manufacturer_code = models.CharField(max_length=50, null=True, blank=True)
    lot_number = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS, default="A")
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="components")

    def __str__(self):
        return f"{self.name} ({self.manufacturer_code or 'N/A'})"