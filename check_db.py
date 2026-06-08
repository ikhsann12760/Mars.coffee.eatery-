import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mars_coffee_project.settings')
django.setup()

def check_connection():
    try:
        # Mencoba melakukan query sederhana ke database
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
        
        db_engine = connection.vendor
        db_name = connection.settings_dict['NAME']
        
        print(f"✅ KONEKSI BERHASIL!")
        print(f"🔹 Database Engine: {db_engine}")
        print(f"🔹 Database Name/URL: {db_name}")
        
        if db_engine == 'postgresql':
            print("🚀 Anda sedang terhubung ke PostgreSQL (Vercel/Production Mode)")
        else:
            print("💻 Anda sedang terhubung ke SQLite (Local/Development Mode)")
            
    except Exception as e:
        print(f"❌ KONEKSI GAGAL!")
        print(f"Error: {e}")

if __name__ == "__main__":
    check_connection()
