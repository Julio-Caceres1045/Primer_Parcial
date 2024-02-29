class Nodo:
    def __init__(self, coef, exp):
        self.coef = coef #Coeficiente del polinomio
        self.exp = exp #Exponente del termino del polinomio
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.head = None #Esta es la cabeza de la lista

    def insertar_termino(self, coef, exp):
        nuevo_nodo = Nodo(coef, exp) #Se creo un nuevo nodo que tendra el coeficiente y el exponente
        if not self.head:
            self.head = nuevo_nodo #Si la lista estuviera vacia este se convierte en cabeza
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def evaluar(self, x):
        resultado = 0
        actual = self.head
        while actual:
            resultado += actual.coef * (x ** actual.exp) #Sumar los valores evaluados en x resultado
            actual = actual.siguiente
        return resultado

    def sumar(self, otro_polinomio):
        resultado = Polinomio()
        actual1 = self.head
        actual2 = otro_polinomio.head
        while actual1 and actual2:
            if actual1.exp > actual2.exp:
                resultado.insertar_termino(actual1.coef, actual1.exp)
                actual1 = actual1.siguiente
            elif actual1.exp < actual2.exp:
                resultado.insertar_termino(actual2.coef, actual2.exp)
                actual2 = actual2.siguiente
            else:
                coef_suma = actual1.coef + actual2.coef
                resultado.insertar_termino(coef_suma, actual1.exp)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
        while actual1:
            resultado.insertar_termino(actual1.coef, actual1.exp)
            actual1 = actual1.siguiente
        while actual2:
            resultado.insertar_termino(actual2.coef, actual2.exp)
            actual2 = actual2.siguiente
        return resultado

    def restar(self, otro_polinomio):
        resultado = Polinomio()
        actual1 = self.head
        actual2 = otro_polinomio.head
        while actual1 and actual2:
            if actual1.exp > actual2.exp:
                resultado.insertar_termino(actual1.coef, actual1.exp)
                actual1 = actual1.siguiente
            elif actual1.exp < actual2.exp:
                resultado.insertar_termino(-actual2.coef, actual2.exp)
                actual2 = actual2.siguiente
            else:
                coef_resta = actual1.coef - actual2.coef
                resultado.insertar_termino(coef_resta, actual1.exp)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
        while actual1:
            resultado.insertar_termino(actual1.coef, actual1.exp)
            actual1 = actual1.siguiente
        while actual2:
            resultado.insertar_termino(-actual2.coef, actual2.exp)
            actual2 = actual2.siguiente
        return resultado
def ingresar_polinomio():
    polinomio = Polinomio()
    grado = int(input("Ingrese el grado del polinomio: ")) #Aca solicito que ingrese el grado mañor del polinomio
    for i in range(grado, -1, -1):
        coef = float(input(f"Ingrese el coeficiente del término de grado {i}: "))  #Aca solicito que ingrese el coeficiente de cada termino
        polinomio.insertar_termino(coef, i)
    return polinomio

def mostrar_polinomio(polinomio, nombre):
    if polinomio.head is None:
        print(f"{nombre} = 0")
        return
    expresion = ""
    actual = polinomio.head
    while actual:
        if actual.exp == 0:
            expresion += f"{actual.coef}"
        elif actual.exp == 1:
            expresion += f"{actual.coef}x"
        else:
            expresion += f"{actual.coef}x^{actual.exp}"
        if actual.siguiente:
            expresion += " + "
        actual = actual.siguiente
    print(f"{nombre} = {expresion}")
def mostrar_menu():
    print("\nMenú:")
    print("1. Ingresar componentes de un polinomio A")
    print("2. Ingresar componentes de un polinomio B")
    print("3. Sumar polinomios A y B")
    print("4. Restar polinomios")
    print("5. Evaluar polinomio")
    print("6. Salir")

polinomio_a = None
polinomio_b = None
resultado = None
while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        polinomio_a = ingresar_polinomio()
        mostrar_polinomio(polinomio_a, "A")
    elif opcion == 2:
        polinomio_b = ingresar_polinomio()
        mostrar_polinomio(polinomio_b, "B")
    elif opcion == 3:
        if polinomio_a is None or polinomio_b is None:
            print("Por favor, ingrese primero los polinomios A y B.")
        else:
            resultado = polinomio_a.sumar(polinomio_b)
            mostrar_polinomio(resultado, "Resultado de la suma")
    elif opcion == 4:
        if polinomio_a is None or polinomio_b is None:
            print("Por favor, ingrese primero los polinomios A y B.")
        else:
            resultado = polinomio_a.restar(polinomio_b)
            mostrar_polinomio(resultado, "Resultado de la resta")
    elif opcion == 5:
        polinomio = None
        if polinomio_a is None and polinomio_b is None:
            print("Por favor, primero ingrese un polinomio.")
        else:
            polinomio_seleccionado = input("Seleccione el polinomio a evaluar (A o B): ")
            if polinomio_seleccionado.lower() == 'a':
                polinomio = polinomio_a
            elif polinomio_seleccionado.lower() == 'b':
                polinomio = polinomio_b
            else:
                print("Polinomio no válido.")
        if polinomio:
            x = float(input("Ingrese el valor de x para evaluar el polinomio: "))
            resultado_evaluado = polinomio.evaluar(x)
            print(f"El resultado de evaluar el polinomio en x={x} es: {resultado_evaluado}")
    elif opcion == 6:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")