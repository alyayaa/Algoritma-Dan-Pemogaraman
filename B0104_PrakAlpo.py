# ========================================================
# (B0104)
# ========================================================

# 1. Pembuktian Pertanyaan No. 1: String + Integer tanpa konversi
print("--- 1. Uji Coba String + Integer ---")
try:
    hasil = "Umur: " + 20
except TypeError as e:
    print("Hasil Error:", e)
    print("Solusi dengan str():", "Umur: " + str(20))
print()

# 2. Pembuktian Pertanyaan No. 2: Tuple (Immutable) untuk Koordinat GPS
print("--- 2. Uji Coba Tuple Koordinat GPS ---")
koordinat_gps = (-6.1751, 106.8650)
print("Koordinat awal:", koordinat_gps)
try:
    # Mencoba mengubah nilai indeks pertama pada Tuple
    koordinat_gps[0] = -7.2575
except TypeError as e:
    print("Hasil Error saat diubah:", e)
print()

# 3. Pembuktian Pertanyaan No. 3: Tipe Data Set Menghapus Duplikat
print("--- 3. Uji Coba Tipe Data Set ---")
data_ganda = {10, 20, 20, 30, 40, 40, 50}
print("Data asli yang diinput : {10, 20, 20, 30, 40, 40, 50}")
print("Hasil tersimpan di Set :", data_ganda)