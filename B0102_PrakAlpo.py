# ==============================================================================
# B0102 (1 x 50 Menit)
# Bagian 2 - Studi Kasus Pengolahan Data Akademik Mahasiswa
# ==============================================================================

# ------------------------------------------------------------------------------
# Langkah 1. Inisialisasi Data Mentah (Menerima Input & Variabel Dasar)
# ------------------------------------------------------------------------------
nim = "261080200018"
nama_mahasiswa = "Aisyiyah Alya Caesar"
is_aktif = True

# Data nilai mentah dari form (bertipe string)
str_nilai_algoritma = "85.5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.25"

print("--- LANGKAH 1: DATA MENTAH MAHASSWA ---")
print("NIM             :", nim)
print("Nama Mahasiswa  :", nama_mahasiswa)
print("Status Aktif    :", is_aktif)
print("Nilai Algo (str):", str_nilai_algoritma, type(str_nilai_algoritma))
print()


# ------------------------------------------------------------------------------
# Langkah 2. Konversi Tipe Data & Kalkulasi (Type Casting & Operation)
# ------------------------------------------------------------------------------
# Konversi dari String ke Float
nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

# Kalkulasi Total dan Rata-rata Nilai
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul

print("--- LANGKAH 2: HASIL KONVERSI & KALKULASI ---")
print("Nilai Algo (float):", nilai_algo, type(nilai_algo))
print("Total Nilai       :", total_nilai)
print("Rata-rata Nilai   :", round(rata_rata_nilai, 2))
print()


# ------------------------------------------------------------------------------
# Langkah 3. Mengatur Data Kompleks dengan Koleksi (List & Dictionary)
# ------------------------------------------------------------------------------
# List untuk daftar mata kuliah
daftar_matkul = ["Algoritma dan Pemrograman", "Basis Data", "Pemrograman Web"]

# Dictionary untuk transkrip nilai mutu (Skala 4.0)
transkrip_nilai = {
    "Algoritma dan Pemrograman": 3.75,
    "Basis Data": 3.00,
    "Pemrograman Web": 4.00
}

# Kalkulasi IPK Sementara
total_bobot = sum(transkrip_nilai.values())
ipk_sementara = total_bobot / len(transkrip_nilai)

print("--- LANGKAH 3: DATA KOLEKSI & IPK SEMENTARA ---")
print("Daftar Mata Kuliah:", daftar_matkul)
print("Transkrip Nilai   :", transkrip_nilai)
print("IPK Sementara     :", round(ipk_sementara, 2))
print()


# ------------------------------------------------------------------------------
# Langkah 4. Pembaruan Variabel (State Update) & Penambahan Data
# ------------------------------------------------------------------------------
# Mahasiswa mengambil mata kuliah susulan / tambahan (Jaringan Komputer)
matkul_baru = "Jaringan Komputer"
nilai_jk = 88.0
bobot_jk = 3.50

# Update List & Dictionary
daftar_matkul.append(matkul_baru)
transkrip_nilai[matkul_baru] = bobot_jk

# Update State Kalkulasi (Total & IPK)
total_nilai = total_nilai + nilai_jk
jumlah_matkul = jumlah_matkul + 1
rata_rata_baru = total_nilai / jumlah_matkul

ipk_terbaru = sum(transkrip_nilai.values()) / len(transkrip_nilai)

print("--- LANGKAH 4: PEMBARUAN DATA (STATE UPDATE) ---")
print(f"Mata kuliah baru '{matkul_baru}' berhasil ditambahkan.")
print("Daftar Matkul Terbaru :", daftar_matkul)
print("Transkrip Terbaru     :", transkrip_nilai)
print("Total Nilai Baru      :", total_nilai)
print("Rata-rata Terbaru     :", round(rata_rata_baru, 2))
print("IPK Terbaru           :", round(ipk_terbaru, 2))