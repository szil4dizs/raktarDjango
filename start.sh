#!/bin/bash

echo "Várakozás az adatbázisra..."
sleep 2  # Biztosítja, hogy az SQLite fájl megfelelően inicializálódjon

echo "Migrációk futtatása..."
python manage.py migrate --noinput

# echo "Statikus fájlok gyűjtése..."
# python manage.py collectstatic --noinput

echo "Admin felhasználó létrehozása..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "Admin123")
    print("Admin felhasználó létrehozva.")
else:
    print("Admin felhasználó már létezik.")
EOF

echo "****************************"
echo "* felhasználó: admin       *"
echo "* jelszó: Admin123         *"
echo "****************************"

# Szerver indítása
exec "$@"