class Ejemplo:
    def metodo_instancia(self):
        return f"Instancia: {self}"

    @classmethod
    def metodo_clase(cls):
        return f"Clase: {cls}"

    @staticmethod
    def metodo_estatico():
        return "No recibe ni self ni cls"

obj = Ejemplo()

print(obj.metodo_instancia())   # ✅ usa self
print(obj.metodo_clase())       # ✅ usa cls
print(obj.metodo_estatico())    # ✅ no necesita nada

print(Ejemplo.metodo_clase())   # también desde la clase
print(Ejemplo.metodo_estatico()) # también desde la clase
