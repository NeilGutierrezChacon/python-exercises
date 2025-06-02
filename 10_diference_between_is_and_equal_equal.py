a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True → tienen el mismo contenido
print(a is b)  # False → son objetos distintos en memoria

c = a
print(a is c)  # True → c y a apuntan al mismo objeto

## Importante.- Esta diferencia se ve más claramente con objetos como listas en cambio si usamos datos primitivos 

x = 100
y = 100
print(x is y)  # True en CPython (por optimización interna)

x = 1000
y = 1000
print(x is y)  # False en muchos casos (no se cachea)

## Esto puede dar True en ambos casos. Esto sucede por que python intermente optimiza y reutiliza objetos para mejorar el rendimiento y uso de memoria para algunos valores basicos.

