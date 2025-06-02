"""
🧪 Ejercicio: Crear un iterador personalizado que itere sobre los números pares hasta un límite
Objetivo:
Define una clase llamada EvenNumbers que sea un iterador para recorrer los números pares desde 0 hasta un límite dado (exclusivo).

"""

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.last_iter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.last_iter = self.current
        if self.current < self.limit:
            self.current += 2
            return self.last_iter
        else:
            raise StopIteration


evens = EvenNumbers(10)
for num in evens:
    print(num)

