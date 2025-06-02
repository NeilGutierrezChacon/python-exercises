import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Ojo: incluye la referencia temporal pasada a getrefcount
