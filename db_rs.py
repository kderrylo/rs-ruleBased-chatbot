import sqlite3
import json

conn = sqlite3.connect('bpjs_hospital.db')
c = conn.cursor()

c.execute('''
CREATE TABLE dokter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    spesialisasi TEXT NOT NULL,
    jadwal TEXT NOT NULL
)
''')

doctors = [
    ("Dr. Ali", "Dokter Umum", json.dumps(["Senin 09:00", "Selasa 10:00", "Rabu 11:00"])),
    ("Dr. Budi", "Kardiolog", json.dumps(["Senin 10:00", "Kamis 12:00"])),
    ("Dr. Chandra", "Neurolog", json.dumps(["Selasa 14:00", "Jumat 15:00"]))
]

c.executemany('''
INSERT INTO dokter (nama, spesialisasi, jadwal)
VALUES (?, ?, ?)
''', doctors)


conn.commit()
conn.close()

print("Database dan tabel berhasil dibuat, data dokter telah ditambahkan.")
