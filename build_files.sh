#!/bin/bash

echo "Building project..."
# Menggunakan --break-system-packages untuk melewati proteksi environment di Vercel baru
python3.12 -m pip install --break-system-packages -r requirements.txt

echo "Collect Static..."
# Penting: Jalankan collectstatic sebelum migrasi untuk memastikan folder static siap
python3.12 manage.py collectstatic --noinput --clear

echo "Make Migrations..."
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput || echo "Migration skipped or failed (this is normal if DB is not accessible during build)"

