class Ejemplo:
    def __init__(self):
        self.existe = None
    def __getattribute__(self, name):
        print(f"__getattribute__ llamado para: {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"__getattr__ llamado para: {name}")
        return "atributo por defecto"

obj = Ejemplo()
obj.existe = 42

print(obj.existe)     # llama __getattribute__, no __getattr__
print(obj.no_existe)  # llama __getattribute__ → falla → llama __getattr__
