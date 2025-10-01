class Calificaciones:
    def __init__(self, calif1, calif2, calif3):
        self.calif1 = calif1
        self.calif2 = calif2
        self.calif3 = calif3
        self.promedio = 0

    def calcular_promedio(self):
        self.promedio = (self.calif1 + self.calif2 + self.calif3) / 3

    def imprimir_promedio(self):
        print("El promedio es:", self.promedio)


# Programa principal
while True:
    print("\nElija una opción:")
    print("1. Agregar calificaciones")
    print("2. Sacar promedio")
    print("3. Salir")
    opcion = input("Seleccione el número de la opción: ")

    if opcion == "1":
        calif1 = float(input("Ingrese calificación 1: "))
        calif2 = float(input("Ingrese calificación 2: "))
        calif3 = float(input("Ingrese calificación 3: "))
        cal = Calificaciones(calif1, calif2, calif3)
        print("Calificaciones agregadas correctamente.")

    elif opcion == "2":
        try:
            cal.calcular_promedio()
            cal.imprimir_promedio()
        except NameError:
            print("Primero debe ingresar calificaciones (opción 1).")

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida, intente de nuevo.")