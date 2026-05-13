usuario = {"nombre": input("Ingrese su nombre: "), "edad" : input("Ingrese su edad: "),
            "profesion": input("Ingrese su profesión: ")}
print("Tu nombre es:")
print(usuario.get("nombre"))
print("Tu edad es:")
print(usuario.get("edad"))
print("Tu profesion es:")
print(usuario.get("profesion"))