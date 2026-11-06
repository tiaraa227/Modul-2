def desimal_ke_biner(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 2) + hasil
        n //= 2
    return hasil

def desimal_ke_oktal(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 8) + hasil
        n //= 8
    return hasil

def desimal_ke_hex(n):
    digit_hex = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = digit_hex[n % 16] + hasil
        n //= 16
    return hasil


# Data perangkat jaringan
perangkat = [
    {"nama": "Router-A",  "id": 192},
    {"nama": "Switch-B",  "id": 255},
    {"nama": "Server-01", "id": 1024},
    {"nama": "PC-Lab",    "id": 42},
    {"nama": "AP-Wifi",   "id": 0},
]

print(f"{'Nama':<12} {'Desimal':>8} {'Biner':>12} {'Oktal':>8} {'Heksadesimal':>14}")
print("=" * 58)

for p in perangkat:
    nama = p["nama"]
    n    = p["id"]
    print(f"{nama:<12} {n:>8} {desimal_ke_biner(n):>12} {desimal_ke_oktal(n):>8} {desimal_ke_hex(n):>14}")

print("\nVerifikasi menggunakan fungsi bawaan Python:")
for p in perangkat:
    n = p["id"]
    print(f"  {p['nama']}: bin={bin(n)}, oct={oct(n)}, hex={hex(n).upper()}")