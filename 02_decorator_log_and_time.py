"""
🧪 Ejercicio: Medidor de tiempo de ejecución y logging
🎯 Objetivo:
Crear un decorador llamado log_and_time que haga lo siguiente:

Imprima el nombre de la función que se está ejecutando.

Imprima los argumentos posicionales y de palabra clave con los que se llamó.

Mida y muestre el tiempo que tarda en ejecutarse la función decorada.

Opcional: Acepte un parámetro para activar o desactivar el log.
"""
import time
import functools

def log_and_time(_func=None, *, enabled=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"Ejecutando función: {func.__name__}")
                print(f"Args: {args}, Kwargs: {kwargs}")
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"Tiempo de ejecución: {end - start:.4f} segundos")
                return result
            else:
                return func(*args, **kwargs)
        return wrapper
    # Si se llama como @log_and_time sin paréntesis
    if _func is not None and callable(_func):
        return decorator(_func)

    # Si se llama como @log_and_time(enabled=True)
    return decorator


@log_and_time
def slow_add(a, b):
    time.sleep(1)
    return a + b

@log_and_time(enabled=False)
def slow_mul(a, b):
    time.sleep(1)
    return a * b

print(slow_add(3, 5))
print(slow_mul(2, 4))