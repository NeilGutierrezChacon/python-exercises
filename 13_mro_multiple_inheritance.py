class A:
    def foo(self):
        print("A.foo")

class B:
    def foo(self):
        print("B.foo")

class C(A, B):  # Hereda primero de A, luego de B
    pass

c = C()
c.foo()  # Imprime "A.foo"
print(C.mro())
