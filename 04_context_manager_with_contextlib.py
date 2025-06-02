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

from contextlib import contextmanager
import time
@contextmanager
def temporizador(name):
    init = time.time()

    if name is None:
        raise Exception("Name is required!!")
    try:
        yield
    finally:
        duration = time.time() - init
        print(f"✅ {name} completado en {duration:.2f} segundos.")


with temporizador("Suma un rango de numeros"):
    sum([i for i in range(10**6)])