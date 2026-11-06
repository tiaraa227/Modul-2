# def desimal_ke_biner(n):
#     """Konversi bilangan desimal ke biner (basis 2)."""
#     if n == 0:
#         return "0"
#     hasil = ""
#     while n > 0:
#         sisa = n % 2
#         hasil = str(sisa) + hasil
#         n = n // 2
#     return hasil


# def desimal_ke_oktal(n):
#     """Konversi bilangan desimal ke oktal (basis 8)."""
#     if n == 0:
#         return "0"
#     hasil = ""
#     while n > 0:
#         sisa = n % 8
#         hasil = str(sisa) + hasil
#         n = n // 8
#     return hasil


# def desimal_ke_hex(n):
#     """Konversi bilangan desimal ke heksadesimal (basis 16)."""
#     digit_hex = "0123456789ABCDEF"
#     if n == 0:
#         return "0"
#     hasil = ""
#     while n > 0:
#         sisa = n % 16
#         hasil = digit_hex[sisa] + hasil
#         n = n // 16
#     return hasil


# def biner_ke_desimal(biner_str):
#     """Konversi bilangan biner (string) ke desimal."""
#     hasil = 0
#     pangkat = 0
#     for digit in reversed(biner_str):
#         hasil += int(digit) * (2 ** pangkat)
#         pangkat += 1
#     return hasil


def desimal_ke_basis(n, basis):
    """Konversi desimal ke basis sembarang (2–16)."""
    digit = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = digit[n % basis] + hasil
        n //= basis
    return hasil


# Uji
angka = 100
for basis in [2, 8, 10, 16]:
    print(f"100 dalam basis {basis:>2}: {desimal_ke_basis(angka, basis)}")