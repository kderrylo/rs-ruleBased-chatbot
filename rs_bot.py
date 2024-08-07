import re
import random
import sqlite3
import json

class BPJSChatbot:
    def __init__(self, db_path):
        self.db_path = db_path
        self.symptoms = []
        self.diagnosis = ""
    
    def greet(self):
        self.name = input("Apa nama Anda?\n")
        will_help = input(f"Halo {self.name}, saya BPJSBot. Saya akan membantu Anda memahami gejala yang Anda alami dan membuat rujukan jika diperlukan. Apakah Anda ingin melanjutkan? (ya/tidak)\n")
        if will_help.lower() in ("tidak", "no", "tidak", "tidak"):
            print("Baiklah, semoga Anda sehat selalu!")
            return
        self.collect_symptoms()
    
    def collect_symptoms(self):
        symptoms = input("Apa saja gejala yang Anda alami? Misalnya, demam, batuk, nyeri, dll.\n")
        self.symptoms = [symptom.strip() for symptom in symptoms.split(',')]
        self.diagnose()
    
    def diagnose(self):
        print("Terima kasih atas informasinya. Berdasarkan gejala yang Anda sebutkan, berikut adalah beberapa kemungkinan:\n")
        
        if "demam" in self.symptoms and "batuk" in self.symptoms:
            self.diagnosis = "Flu atau infeksi pernapasan"
        elif "nyeri dada" in self.symptoms and "sesak napas" in self.symptoms:
            self.diagnosis = "Masalah jantung"
        elif "sakit kepala" in self.symptoms and "mual" in self.symptoms:
            self.diagnosis = "Migrain atau tekanan darah tinggi"
        
        print(f"- Anda mungkin mengalami {self.diagnosis}.\n")
        print("Harap diingat bahwa saya bukan seorang dokter. Untuk diagnosis dan perawatan yang akurat, sebaiknya Anda berkonsultasi dengan dokter.")
        self.offer_referral()
    
    def offer_referral(self):
        need_referral = input("Apakah Anda ingin membuat rujukan ke spesialis? (ya/tidak)\n")
        if need_referral.lower() in ("ya", "yes", "y"):
            self.select_doctor()
        else:
            print("Baiklah, semoga Anda cepat sembuh dan tetap sehat!")
    
    def select_doctor(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        
        if self.diagnosis == "Flu atau infeksi pernapasan":
            specialization = "Dokter Umum"
        elif self.diagnosis == "Masalah jantung":
            specialization = "Kardiolog"
        elif self.diagnosis == "Migrain atau tekanan darah tinggi":
            specialization = "Neurolog"
        
        cursor.execute("SELECT id, nama, jadwal FROM dokter WHERE spesialisasi = ?", (specialization,))
        doctors = cursor.fetchall()
        
        if not doctors:
            print(f"Maaf, tidak ada dokter dengan spesialisasi {specialization} yang tersedia.")
            return
        
        print(f"Dokter dengan spesialisasi {specialization} yang tersedia:\n")
        for doc in doctors:
            doc_id, doc_name, doc_schedule = doc
            schedule = json.loads(doc_schedule)
            print(f"ID: {doc_id}, Nama: {doc_name}, Jadwal: {schedule}")
        
        selected_doc_id = int(input("Masukkan ID dokter yang ingin Anda pilih:\n"))
        selected_doc_time = input("Masukkan waktu yang Anda inginkan (misalnya, Senin 10:00):\n")
        
        cursor.execute("SELECT nama, jadwal FROM dokter WHERE id = ?", (selected_doc_id,))
        selected_doc = cursor.fetchone()
        if selected_doc:
            doc_name, doc_schedule = selected_doc
            schedule = json.loads(doc_schedule)
            if selected_doc_time in schedule:
                print(f"Rujukan Anda berhasil dibuat dengan Dr. {doc_name} pada {selected_doc_time}.")
            else:
                print("Maaf, waktu yang Anda pilih tidak tersedia.")
        else:
            print("ID dokter tidak valid.")
        
        connection.close()
    
bot = BPJSChatbot("bpjs_hospital.db")
bot.greet()
