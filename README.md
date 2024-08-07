# BPJSBot

## Deskripsi

BPJS Chatbot adalah aplikasi chatbot yang dirancang untuk membantu pengguna BPJS Kesehatan di rumah sakit dengan melakukan diagnosis awal penyakit, menawarkan rujukan ke spesialis, dan memberikan pilihan dokter serta jadwal yang tersedia berdasarkan diagnosis.

## Fitur

- **Diagnosis Awal**: Mengumpulkan gejala dari pengguna dan memberikan diagnosis awal berdasarkan gejala tersebut.
- **Rujukan ke Spesialis**: Menawarkan opsi untuk membuat rujukan ke spesialis berdasarkan diagnosis awal.
- **Pemilihan Dokter**: Memberikan daftar dokter yang sesuai dengan spesialisasi yang dibutuhkan serta jadwal praktek mereka.

## Cara Menggunakan

1. **Instalasi**:
   - Pastikan Anda memiliki Python terinstal di sistem Anda.
   - Instal dependensi yang diperlukan (jika ada).

2. **Menyiapkan Database**:
   - Jalankan `create_db.py` untuk membuat database dan tabel serta mengisi data dokter.
   
   ```bash
   python create_db.py

3. **Menjalankan Chatbot**:
   - Jalankan script chatbot.
   
   ```bash
   python bpjs_chatbot.py

   
4. **Interaksi**:
   - Ikuti instruksi di terminal untuk memasukkan nama, gejala, dan memilih dokter.

## Struktur Proyek
- create_db.py: Script untuk membuat database dan tabel dokter.
- bpjs_chatbot.py: Script utama chatbot untuk diagnosis dan pembuatan rujukan.
- bpjs_hospital.db: File database SQLite yang berisi data dokter (jangan di-upload ke GitHub jika berisi data sensitif).

  
## Kontribusi
- Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request dengan deskripsi perubahan yang Anda buat.
