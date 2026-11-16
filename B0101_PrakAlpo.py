# ==========================================
# B0101
# ==========================================
# 1. Deklarasi Variabel Sederhana
nama_depan = "Alya"
umur = 18
tinggi_badan = 156
is_aktif = True

# Menampilkan nilai variabel
print("=== LANGKAH 1: VARIABEL & PENAMAAN ===")
print("Nama:", nama_depan)
print("Umur:", umur, "tahun")
print("Tinggi:", tinggi_badan, "cm")
print("Status Aktif:", is_aktif)
print()

# ==========================================
# LANGKAH 2: Tipe Data Dasar (Primitive)
# ==========================================
# Deklarasi berbagai tipe data dasar
angka_bulat = 16          # Integer (int)
angka_desimal = 3,14      # Float (float)
teks = "Belajar Python"   # String (str)
status = False            # Boolean (bool)

# Mengecek tipe data masing-masing variabel
print("=== LANGKAH 2: TIPE DATA DASAR ===")
print("Tipe data angka_bulat  :", type(angka_bulat))
print("Tipe data angka_desimal:", type(angka_desimal))
print("Tipe data teks         :", type(teks))
print("Tipe data status       :", type(status))
print()

# ==========================================
# LANGKAH 3: Tipe Data Koleksi (Non-Primitive)
# ==========================================
print("=== LANGKAH 3: TIPE DATA KOLEKSI ===")
# 1. LIST (Berurutan, bisa diubah / mutable)
hobi = ["Membaca", "Coding", "Berenang"]
print("List Hobi:", hobi)
print("Tipe     :", type(hobi))

# 2. TUPLE (Berurutan, TIDAK bisa diubah / immutable)
koordinat = (-6.1751, 106.8650)
print("Tuple Koordinat:", koordinat)
print("Tipe           :", type(koordinat))

# 3. DICTIONARY (Pasangan Key: Value)
mahasiswa = {
    "nama": "Aisyiyah Alya Caesar",
    "nim": "261080200018",
    "ipk": 3.85
}
print("Dict Mahasiswa:", mahasiswa)
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Tipe          :", type(mahasiswa))

# 4. SET (Nilai unik, tidak berurutan, tidak ada duplikat)
angka_unik = {1, 2, 6, 3, 4, 4, 5}
print("Set Angka Unik:", angka_unik)
print("Tipe          :", type(angka_unik))
print()

# ==========================================
# LANGKAH 4: Konversi Tipe Data (Type Casting)
# ==========================================
print("=== LANGKAH 4: TYPE CASTING ===")
# 1. Konversi dari String ke Integer
str_angka = "960"
int_angka = int(str_angka)
print("Hasil Penjumlahan (100+50):", int_angka + 50)

# 2. Konversi dari Float ke Integer (Angka di belakang koma dipotong)
ipk_float = 3.75
ipk_int = int(ipk_float)
print("Float ke Int:", ipk_int)

# 3. Konversi dari Integer ke String
tahun = 2024
pesan = "Tahun saat ini: " + str(tahun)
print(pesan)

# 4. Konversi dari List ke Set (Menghapus elemen duplikat)
daftar_buah = ["Apel", "Jeruk", "Apel", "Pisang", "Jeruk"]
buah_unik = set(daftar_buah)
print("Buah Unik:", buah_unik)