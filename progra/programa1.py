class Empleado:
    def __init__(self):
        self.n = input("Nombre? ")
        self.s = float(input("Sueldo? "))
        self.h = float(input("Horas? "))
        self.f = input("Ingreso? ")
        self.v = int(input("Semanas? "))

    def ver(self):
        print("Nombre:", self.n)
        print("Sueldo:", self.s)
        print("Horas:", self.h)
        print("Ingreso:", self.f)
        print("Semanas:", self.v)

    def imp(self):
        if self.s > 3000:
            print("Paga impuestos")
        else:
            print("No paga")

    def ht(self):
        if self.h > 8:
            print("Trabajó bien")
        else:
            print("Trabajó poco")

    def vacas(self):
        if self.v > 300:
            print("Tiene vacaciones")
        else:
            print("No tiene vacaciones")

e = Empleado()
e.ver()
e.imp()
e.ht()
e.vacas()