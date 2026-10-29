class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} mulai berlari!")

    def ambil_koin(self, jumlah):
        if self.is_running:
            self.koin += jumlah
            self.skor += jumlah
            print(f"{self.nama} mendapatkan {jumlah} koin!")
        else:
            print("Game sudah berakhir!")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! Game Over!")

    def info_player(self):
        print("\n=== STATUS PEMAIN ===")
        print(f"Nama       : {self.nama}")
        print(f"Skor       : {self.skor}")
        print(f"Jumlah Koin: {self.koin}")
        print(f"Sedang Berlari: {self.is_running}")


# --- PENGUJIAN OBJEK ---
player1 = KarakterSurfer("Jake")

player1.berlari()
player1.ambil_koin(10)
player1.ambil_koin(5)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()