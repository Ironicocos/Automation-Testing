def Sumar():
    try:
        x = 0
        y = 0
        x = int(input("Ingrese un número: "))
        y = int(input("Ingrese un número: "))
        return(x + y)
    except ValueError:
        print("Tienes que ingresar un numero válido")
def Restar():
    try:
        x = 0
        y = 0
        x = int(input("Ingrese un número: "))
        y = int(input("Ingrese un número: "))
        return(x - y)
    except ValueError:
        print("Tienes que ingresar un numero válido")
def Dividir():
    try:
        x = 0
        y = 0
        x = int(input("Ingrese un número: "))
        y = int(input("Ingrese un número: "))
        return(x / y)
    except ValueError:
        print("Tienes que ingresar un numero válido")
    except ZeroDivisionError:
        print("La división por cero no se encuentra definida")
def Multiplicar():
    try:
        x = 0
        y = 0
        x = int(input("Ingrese un número: "))
        y = int(input("Ingrese un número: "))
        return (x * y)
    except ValueError:
        print("Tienes que ingresar un numero válido")