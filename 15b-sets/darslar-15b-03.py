"""
29/03/2021

Dasturlash asoslari

15-DARS: To'plamlar

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
# To'plamlar ustida amallar

# Jamlanma
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = A | B
print(C)
D = A.union(B)
print(D)

# Kesishma
print(A & B)
print(A.intersection(B))

# Farq
print(A - B)
print(B.difference(A))

# Simmetrik farq
print(A ^ B)
print(A.symmetric_difference(B))
