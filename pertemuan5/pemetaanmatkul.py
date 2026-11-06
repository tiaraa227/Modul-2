# Domain: mahasiswa, Kodomain: mata kuliah
mahasiswa   = {"Ani", "Budi", "Citra", "Deni"}
mata_kuliah = {"MatDis", "Algoritma", "Basis Data", "Jaringan"}

# Hubungan sebagai dictionary (setiap mahasiswa → satu matkul)
pemetaan = {
    "Ani"  : "MatDis",
    "Budi" : "Algoritma",
    "Citra": "MatDis",
    "Deni" : "Basis Data",
}

# Apakah ini sebuah fungsi?
# Fungsi: setiap elemen domain dipetakan ke tepat satu elemen kodomain
adalah_fungsi = len(pemetaan) == len(mahasiswa) and \
                all(v in mata_kuliah for v in pemetaan.values())
print("Apakah merupakan fungsi?", adalah_fungsi)

# Range (output yang benar-benar dihasilkan)
range_fungsi = set(pemetaan.values())
print("Range:", range_fungsi)
print("Kodomain:", mata_kuliah)

# Injektif: tidak ada dua mahasiswa → matkul yang sama
values = list(pemetaan.values())
injektif = len(values) == len(set(values))
print("Injektif (one-to-one)?", injektif)

# Surjektif: range = kodomain
surjektif = range_fungsi == mata_kuliah
print("Surjektif (onto)?", surjektif)

# Bijektif
bijektif = injektif and surjektif
print("Bijektif?", bijektif)

# Analisis
print("\n--- Analisis ---")
for mhs, mk in pemetaan.items():
    print(f"  {mhs:6} → {mk}")