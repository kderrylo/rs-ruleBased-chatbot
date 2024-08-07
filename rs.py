import re

class Bot:
    def __init__(self):
        self.symptoms = []
        self.health_history = []
        self.current_conditions = []
    
    def greet(self):
        self.name = input("Apa nama Anda?\n")
        will_help = input(f"Halo {self.name}, saya MediBot. Saya akan membantu Anda memahami gejala yang Anda alami. Apakah Anda ingin melanjutkan? (ya/tidak)\n")
        if will_help.lower() in ("tidak", "no", "tidak", "tidak"):
            print("Baiklah, semoga Anda sehat selalu!")
            return
        self.collect_symptoms()
    
    def collect_symptoms(self):
        symptoms = input("Apa saja gejala yang Anda alami? Misalnya, demam, batuk, nyeri, dll.\n")
        self.symptoms = [symptom.strip() for symptom in symptoms.split(',')]
        self.collect_health_history()
    
    def collect_health_history(self):
        health_history = input("Apakah Anda memiliki riwayat penyakit kronis seperti diabetes atau hipertensi? Jika ya, sebutkan. Jika tidak, ketik 'tidak'.\n")
        if health_history.lower() != "tidak":
            self.health_history = [condition.strip() for condition in health_history.split(',')]
        self.collect_current_conditions()
    
    def collect_current_conditions(self):
        current_conditions = input("Apakah Anda baru-baru ini melakukan perjalanan ke daerah dengan wabah penyakit atau mengalami perubahan kondisi kesehatan? Jika ya, sebutkan. Jika tidak, ketik 'tidak'.\n")
        if current_conditions.lower() != "tidak":
            self.current_conditions = [condition.strip() for condition in current_conditions.split(',')]
        self.diagnose()
    
    def diagnose(self):
        print("Terima kasih atas informasinya. Berdasarkan gejala yang Anda sebutkan, berikut adalah beberapa kemungkinan:\n")

        if "demam" in self.symptoms and "batuk" in self.symptoms:
            print("- Anda mungkin mengalami flu atau infeksi pernapasan.")
        if "nyeri dada" in self.symptoms and "sesak napas" in self.symptoms:
            print("- Anda mungkin mengalami masalah jantung. Segera konsultasikan dengan dokter.")
        if "sakit kepala" in self.symptoms and "mual" in self.symptoms:
            print("- Anda mungkin mengalami migrain atau tekanan darah tinggi.")
        
        print("\nHarap diingat bahwa saya bukan seorang dokter. Untuk diagnosis dan perawatan yang akurat, sebaiknya Anda berkonsultasi dengan dokter.")
        self.monitor_symptoms()
    
    def monitor_symptoms(self):
        follow_up = input("Apakah Anda ingin memantau gejala Anda dari waktu ke waktu? (ya/tidak)\n")
        if follow_up.lower() in ("ya", "yes", "y"):
            print("Baiklah, saya akan membantu Anda memantau gejala Anda. Tetap perhatikan kesehatan Anda dan jangan ragu untuk berkonsultasi dengan dokter.")
        else:
            print("Baiklah, semoga Anda cepat sembuh dan tetap sehat!")

bot = Bot()
bot.greet()
