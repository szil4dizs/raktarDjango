from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name="Bolt neve")

    class Meta:
        verbose_name = "Bolt"
        verbose_name_plural = "Boltok"

    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, verbose_name="Számlaszám (vagy megrendelési szám)")
    purchase_date = models.DateField(verbose_name="Vásárlás dátuma")
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, verbose_name="Bolt neve")

    class Meta:
        verbose_name = "Számla"
        verbose_name_plural = "Számlák"

    def __str__(self): 
        return f"{self.invoice_number} | {self.purchase_date} | {self.store.name if self.store else 'N/A'}" #a lenyíló mezőben a bolt neve is megjelenik


class Machine(models.Model):
    STATUS = [
        ("A", "Aktív"),
        ("I", "Inaktív"),
        ("H", "Hiány"),
    ]

    name = models.CharField(max_length=255, verbose_name="Név")
    type = models.CharField(max_length=255, null=True, blank=True, verbose_name="Típus")
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name="Leírás")
    manufacturer_code = models.CharField(max_length=50, null=True, blank=True, verbose_name="Gyártói cikkszám")
    lot_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Sarzs szám")
    serial_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Sorozatszám")
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, verbose_name="Számla")
    price = models.IntegerField(verbose_name="Ár")
    status = models.CharField(max_length=1, choices=STATUS, default="A", verbose_name="Státusz")
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="components", verbose_name="Kapcsolódó szett")

    class Meta:
        verbose_name = "Eszköz"
        verbose_name_plural = "Eszközök"

    def __str__(self):
        return f"{self.name} ({self.manufacturer_code or ''}) ({self.type or ''})" #a lenyíló mezőben a gyártói cikkszám is megjelenik