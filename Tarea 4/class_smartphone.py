class Nodo:
    def __init__(self, valor, siguiente= None):
        self.valor = valor
        self.siguiente = siguiente

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

class Smartphone:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        if self.cabeza is None:
            print('Está vacia')
        else:
            print('No está vacia')

    def get_tamanio(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.get_siguiente()
        return contador

    def agregar_al_final(self, dato):
        nodo_nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nodo_nuevo
        else:
            actual = self.cabeza
            while actual.get_siguiente() is not None:
                actual = actual.siguiente
            actual.set_siguiente(nodo_nuevo)

    def agregar_al_inicio(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.cabeza
        self.cabeza = nodo_nuevo



    def agregar_despues_de(self, valor, referencia):
        nodo_nuevo = Nodo(valor)
        actual = self.cabeza
        while actual.dato != referencia:
            actual = actual.siguiente
        nodo_nuevo.siguiente = actual.siguiente
        actual.siguiente = nodo_nuevo

    def eliminar_posicion(self, posicion):
        contador = 1
        actual = self.cabeza
        if posicion == 1:
            self.cabeza = actual.get_siguiente()
        else:
            while contador < posicion - 1:
                actual = actual.get_siguiente()
                contador += 1
            actual.set_siguiente(actual.get_siguiente().get_siguiente())

    def eliminar_primero(self):
        actual = self.cabeza
        self.cabeza = actual.get_siguiente()

    def eliminar_el_final(self):
        tamanio = self.get_tamanio()
        actual = self.cabeza
        contador = 2
        while contador < tamanio:
            actual = actual.get_siguiente()
            contador += 1
        actual.set_siguiente(None)

    def buscar_valor(self, valor):
        actual = self.cabeza
        contador = 1
        while actual.valor != valor:
            actual = actual.get_siguiente()
            contador += 1
        print(f' El valor {valor} se ubica en la posición {contador}')

    def actualizar(self,a_buscar,valor):
        actual = self.cabeza
        while actual.valor != a_buscar:
            actual = actual.siguiente
        actual.set_valor(valor)

    def transversal(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor, end=' -> ')
            actual = actual.get_siguiente()
        print('None')