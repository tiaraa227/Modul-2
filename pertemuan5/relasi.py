# # Cartesian product
# # from itertools import product

# A = {1, 2, 3}
# B = {'a', 'b'}

# # cartesian = set(product(A, B))
# # print("A × B:", cartesian)

# # Definisikan relasi sebagai himpunan pasangan
# R = {(1, 'a'), (2, 'b'), (3, 'a')}
# # print("Relasi R:", R)

# # # Matriks relasi
# A_list = sorted(A)
# B_list = sorted(B)

# print("\nMatriks Relasi R:")
# print(f"{'':>4}", end="")
# for b in B_list:
#     print(f"{b:>4}", end="")
# print()

# for a in A_list:
#     print(f"{a:>4}", end="")
#     for b in B_list:
#         print(f"{1 if (a, b) in R else 0:>4}", end="")
#     print()

# Memeriksa sifat relasi pada A ke A
A = {1, 2, 3}

# Relasi "kurang dari atau sama dengan"
R = {(a, b) for a in A for b in A if a <= b}
# print("Relasi R (a ≤ b):", R)

# Refleksif: setiap (a, a) ada dalam R
refleksif = all((a, a) in R for a in A)
# print("Refleksif:", refleksif)

# # Simetris: jika (a,b) ada, maka (b,a) juga ada
# simetris = all((b, a) in R for (a, b) in R)
# print("Simetris:", simetris)

# # Antisimetris: jika (a,b) dan (b,a) ada, maka a == b
# antisimetris = all(a == b for (a, b) in R if (b, a) in R)
# print("Antisimetris:", antisimetris)

# # Transitif: jika (a,b) dan (b,c) ada, maka (a,c) juga ada
transitif = all((a, c) in R for (a, b) in R for (b2, c) in R if b == b2)
print("Transitif:", transitif)