"""
🧪 Ejercicio: Context Manager para temporizador
🎯 Objetivo:
Crear un context manager personalizado llamado Timer que mida el tiempo que tarda en ejecutarse un bloque de código.

🔧 Instrucciones:
Define una clase Timer que implemente los métodos __enter__ y __exit__.

Al entrar al contexto (__enter__):

Guarda el tiempo actual (inicio).

Al salir del contexto (__exit__):

Calcula el tiempo transcurrido.

Imprime el tiempo en segundos.
"""

import time

# Tu clase Timer va aquí

class Timer:
    def __init__(self, message):
        self.message = message
        self.start_time = None
        self.end_time = None
    def __enter__(self):
        self.start_time = time.time()
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"Tiempo de ejecución {end_time - self.start_time:.4f}, {self.message}")
        pass

with Timer("Bloque 1"):
    time.sleep(1.2)

with Timer("Bloque 2"):
    time.sleep(0.5)