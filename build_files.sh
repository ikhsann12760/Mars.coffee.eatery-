#!/bin/bash

echo "Building project..."
# Menggunakan --break-system-packages untuk melewati proteksi environment di Vercel baru
python3.12 -m pip install --break-system-packages -r requirements.txt

echo "Collect Static..."
# Menambahkan --no-input agar tidak berhenti meminta konfirmasi
python3.12 manage.py collectstatic --noinput --clear

echo "Build Completed."

