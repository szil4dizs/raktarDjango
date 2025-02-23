import os
import shutil
from django.shortcuts import render, get_object_or_404, redirect
from .models import Store, Invoice, Machine
from django.http import HttpResponse, HttpRequest
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import default_storage

# Create your views here.
def inventory_list(request):
    machines = Machine.objects.filter(parent__isnull=True).prefetch_related("components")
    hierarchy = []
    for machine in machines:
        entry = {"machine": machine, "components": list(machine.components.all())}
        hierarchy.append(entry)

    return render(request, 'raktar/inventory_list.html', {"hierarchy": hierarchy})
    
def inventory_details(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    components = machine.components.all() 
    
    context = {
        "machine": machine,
        "components": components,
    }
    return render(request, "raktar/inventory_details.html", context)


def backup_database(request):
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    backup_path = os.path.join(settings.BASE_DIR, 'db_backup.sqlite3')
    shutil.copy2(db_path, backup_path)

    # Fájl letöltése
    with open(backup_path, 'rb') as backup_file:
        response = HttpResponse(backup_file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(backup_path)}"'

    # Fájl törlése a letöltés után
    os.remove(backup_path)
    
    return response

def restore_database(request: HttpRequest):
    if request.method == "POST" and request.FILES.get("backup_file"):
        backup_file = request.FILES["backup_file"]
        backup_path = os.path.join(settings.BASE_DIR, "db_restore.sqlite3")

        try:
            # Ideiglenesen mentjük a feltöltött fájlt
            with open(backup_path, "wb+") as destination:
                for chunk in backup_file.chunks():
                    destination.write(chunk)

            # Felülírjuk az eredeti adatbázist
            db_path = os.path.join(settings.BASE_DIR, "db.sqlite3")
            shutil.copy2(backup_path, db_path)

            messages.success(request, "Az adatbázis visszaállítása sikeres!")

        except Exception as e:
            messages.error(request, f"Hiba történt az adatbázis visszaállítása során: {e}")

        finally:
            # Fájl törlése a visszaállítás után
            if os.path.exists(backup_path):
                os.remove(backup_path)

        return redirect("restore_database")

    return render(request, "raktar/restore.html")