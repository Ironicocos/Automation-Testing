def Sumar(x, y):
    try:
        #x = int(input("Ingrese un número: "))
        #y = int(input("Ingrese un número: "))
        return(x + y)
    except TypeError:
        print("Tienes que ingresar un numero válido")
    except ValueError:
        print("Tienes que ingresar un número válido")
def Restar(x, y):
    try:
        #x = int(input("Ingrese un número: "))
        #y = int(input("Ingrese un número: "))
        return(x - y)
    except TypeError:
        print("Tienes que ingresar un numero válido")
    except ValueError:
        print("Tienes que ingresar un numero válido")
def Dividir(x, y):
    try:
        #x = int(input("Ingrese un número: "))
        #y = int(input("Ingrese un número: "))
        return(x / y)
    except TypeError:
        print("Tienes que ingresar un numero válido")
    except ValueError:
        print("Tienes que ingresar un numero válido")
    except ZeroDivisionError:
        print("La división por cero no se encuentra definida")
def Multiplicar(x, y):
    try:
        #x = int(input("Ingrese un número: "))
        #y = int(input("Ingrese un número: "))
        return (x * y)
    except TypeError:
        print("Tienes que ingresar un numero válido")
    except ValueError:
        print("Tienes que ingresar un numero válido")