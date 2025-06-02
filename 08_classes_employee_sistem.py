"""
🧩 Ejercicio: Sistema de empleados
Imagina que estás desarrollando un pequeño sistema de nómina para una empresa.

🎯 Requisitos:
Crear una clase base Empleado con:

Atributos: nombre, apellido, salario_base.

Un método nombre_completo que retorne el nombre completo del empleado.

Una propiedad salario que pueda ser sobreescrita por subclases.

Crear dos clases hijas:

EmpleadoTiempoCompleto: que hereda de Empleado.

Tiene un bono_anual, y el salario total incluye el bono.

EmpleadoPorHora: que hereda de Empleado.

Tiene atributos horas_trabajadas y tarifa_hora, y su salario se calcula con esos datos.

Encapsular los atributos con _ y usar @property para exponer salario, nombre_completo y otros datos necesarios.
"""

class Empleado():
    def __init__(self, nombre, apellido, salario_base):
        self._nombre = nombre
        self._apellido = apellido
        self._salario_base = salario_base

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"
    
    @property
    def salario(self):
        return self._salario_base
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono):
        super().__init__(nombre,apellido,salario_base)
        self._bono = bono

    @property
    def salario(self):
        return self._salario_base + self._bono 
    
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, tarifa_horas, horas_trabajadas):
        super().__init__(nombre,apellido,0)
        self._tarifa_horas = tarifa_horas
        self._horas_trabajadas = horas_trabajadas

    @property
    def salario(self):
        return self._tarifa_horas * self._horas_trabajadas
        
    

e1 = EmpleadoTiempoCompleto("Ana", "Gómez", 3000, 500)
e2 = EmpleadoPorHora("Luis", "Pérez", 20, 120)

print(e1.nombre_completo, "→", e1.salario, "EUR")
print(e2.nombre_completo, "→", e2.salario, "EUR")
