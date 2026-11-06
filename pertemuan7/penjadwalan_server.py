import math

def adalah_genap(n):
    return n % 2 == 0

def hitung_modulus(n, m):
    return n % m

def cari_faktor(n):
    faktor = []
    for i in range(1, n + 1):
        if n % i == 0:
            faktor.append(i)
    return faktor

def adalah_prima(n):
    if n<= 1:
        return False
    if n == 2:
        return True
    if n % 2 :
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kpk(a, b):
    return abs(a * b) // fpb(a, b)



bilangan_uji = [1, 2, 7, 12, 17, 24, 36, 97, 100]

print("=" * 55)
print(f"{'Bilangan':>10} {'Genap?':>8} {'Prima?':>8} {'Faktor'}")
print("=" * 55)
for n in bilangan_uji:
    print(f"{n:>10} {str(adalah_genap(n)):>8} {str(adalah_prima(n)):>8} {cari_faktor(n)}")

print()
pasangan = [(12, 18), (48, 36), (7, 13), (100, 75)]
print(f"{'(a, b)':>12} {'FPB':>6} {'KPK':>8}")
print("-" * 30)
for a, b in pasangan:
    print(f"({a:>3}, {b:>3})  {fpb(a, b):>6} {kpk(a,b):>8}")

def sieve_of_eratosthenes(batas):
    """Mencari semua bilangan prima dari 2 hingga batas."""
    prima = [True] * (batas + 1)
    prima[0] = prima[1] = False

    p = 2
    while p * p <= batas:
        if prima[p]:

             for i in range(p* p, batas + 1, p):
                 prima[i] = False
        p += 1

    return [n for n in range(2, batas + 1) if prima[n]]

prima_100 = sieve_of_eratosthenes(100)
print(f"Bilangan prima hingga 100 ({len(prima_100)} bilangan):")
print(prima_100)

def periksa_id_perangkat(daftar_id):
    print("\nVerifikasi ID Perangkat:")
    print(f"{'ID':>8} {'Prima?':>8} {'Keterangan'}")
    print("-" * 35)
    for id_perangkat in daftar_id:
        status = adalah_prima(id_perangkat)
        ket = "Dapat digunakan sebagai kunci" if status else "Bukan bilangan prima"
        print(f"{id_perangkat:>8} {str(status):>8}  {ket}")

daftar_id_uji = [7, 11, 15, 23, 49, 97, 100, 101]
periksa_id_perangkat(daftar_id_uji)