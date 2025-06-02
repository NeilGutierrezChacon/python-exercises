"""
✅ Requisitos de la extensión:
No modificar las clases existentes (Empleado, EmpleadoTiempoCompleto, EmpleadoPorHora).

Añadir una nueva funcionalidad que utilice:

Interfaces (clases abstractas).

Getters y setters (usando @property).

Todo debe construirse como una extensión encima del código base.

🎯 Objetivo de la extensión
Vamos a añadir un sistema de evaluación de desempeño para ciertos empleados, que afecte su información sin alterar la clase base.

🧱 Estructura de la extensión
Una nueva interfaz Evaluable que define:

una propiedad desempeño (con getter y setter)

un método bono_por_desempeño()

Una nueva clase EmpleadoEvaluado, que:

recibe una instancia de un empleado existente.

expone su nombre_completo y salario delegando.

implementa la interfaz y agrega lógica de evaluación.
"""

from abc import ABC, abstractmethod

##### NO MODIFICAR!!!
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
        
##### NO MODIFICAR!!!        

from enum import Enum

class NivelDesempeño(Enum):
    ALTO = "alto"
    MEDIO = "medio"
    BAJO = "bajo"

class Evaluable(ABC):

    @property
    @abstractmethod
    def desempeño(self):
        pass

    @desempeño.setter
    @abstractmethod
    def desempeño(self):
        pass

    @abstractmethod
    def bono_por_desempeño(self):
        pass

class EmpleadoEvaluado(Evaluable):
    def __init__(self, empleado: Empleado):
        self._empleado = empleado
        self._desempeño = None

    @property
    def nombre_completo(self):
        return self._empleado.nombre_completo
    
    @property
    def salario(self):
        return self._empleado.salario

    @property
    def desempeño(self):
        return self._desempeño
    
    @desempeño.setter
    def desempeño(self, valor):
        if not isinstance(valor, NivelDesempeño):
            raise ValueError(f"El desempeño debe ser { [d.value for d in NivelDesempeño]  }")
        self._desempeño = valor

    def bono_por_desempeño(self):
        if self._desempeño == NivelDesempeño.ALTO:
            return self.salario * 0.10
        elif self._desempeño == NivelDesempeño.MEDIO:
            return self.salario * 0.05
        return 0


base = EmpleadoTiempoCompleto("Ana", "López", 3000, 500)

evaluado = EmpleadoEvaluado(base)
evaluado.desempeño = NivelDesempeño.BAJO

print(f"{evaluado.nombre_completo}")
print(f"Salario base: {evaluado.salario}")
print(f"Desempeño: {evaluado.desempeño.value}")
print(f"Bono por desempeño: {evaluado.bono_por_desempeño()}")