# ==========================================
# B0103
# ==========================================
nama_hero = "Arthur"  # String
level = 10  # Integer
hp = 150.5  # Float
is_alive = True  # Boolean
inventory = ["Pedang Kayu", "Perisai Besi", "Panah"]  # List
atribut = {"kekuatan": 80, "kelincahan": 65}  # Dictionary

# ==========================================
# 2. TAMPILKAN SELURUH INFORMASI KARAKTER
# ==========================================
print("=== PROFIL KARAKTER AWAL ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Status    :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)
print()

# ==========================================
# 3. TAMPILKAN TIPE DATA MASING-MASING VARIABEL
# ==========================================
print("=== TIPE DATA VARIABEL ===")
print("Tipe data nama_hero :", type(nama_hero))
print("Tipe data level     :", type(level))
print("Tipe data hp        :", type(hp))
print("Tipe data is_alive  :", type(is_alive))
print("Tipe data inventory :", type(inventory))
print("Tipe data atribut   :", type(atribut))
print()

# ==========================================
# 4. KERJAKAN AKSI (UPDATE DATA)
# ==========================================
# A. Tambahkan item "Ramuan HP" ke dalam inventory (List)
inventory.append("Ramuan HP")

# B. Konversi level ke float lalu tambahkan 0.5
level_float = float(level)
level = level_float + 0.5

# ==========================================
# 5. CETAK KEMBALI INFORMASI TERBARU
# ==========================================
print("=== PROFIL KARAKTER SETELAH AKSI (UPDATE) ===")
print("Nama Hero :", nama_hero)
print("Level Baru:", level, "(Tipe Data:", type(level), ")")
print("HP        :", hp)
print("Status    :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)