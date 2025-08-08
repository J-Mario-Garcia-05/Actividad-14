def ordenar_nombre(nombres):
    if len(nombres) <= 1:
        return nombres
    pivote = nombres[0]
    menores = [x for x in nombres[1:] if x["nombre"].lower() < pivote['nombre'].lower()]
    iguales = [x for x in nombres if x['nombre'].lower() == pivote['nombre'].lower()]
    mayores = [x for x in nombres[1:] if x['nombre'].lower() > pivote['nombre'].lower()]
    return ordenar_nombre(menores) + iguales +ordenar_nombre(mayores)

def ordenar_edad(edades):
    if len(edades) <= 1:
        return edades
    pivote = edades[0]
    menores = [x for x in edades[1:] if x['edad'] < pivote['edad']]
    iguales = [x for x in edades if x['edad'] == pivote['edad']]
    mayores = [x for x in edades if x['edad'] > pivote['edad']]
    return ordenar_edad(menores) + iguales + ordenar_edad(mayores)

participantes = {}
dorsal = 1001
opcion = 0
while opcion != 4:
    print("--MENÚ DE OPCIONES--")
    print("1.Agregar participantes")
    print("2.Mostrar participantes ordenados por nombre")
    print("3.Mostrar participantes ordenados por edad")
    print("4.Salir")
    try:
        opcion = int(input("\nSeleccione una opción: "))
        match opcion:
            case 1:
                cantidad = int(input("¿Cuántos participante desea agregar? (1-10): "))
                if cantidad < 0 or cantidad > 10:
                    print("Cantidad ingresada fuera de rango")
                    continue
                for i in range(cantidad):
                    print(f"Datos del participante {i + 1}:")
                    nombre = input("\tNombre completo: ")
                    edad = int(input("\tEdad: "))
                    if edad < 10 or edad > 60:
                        print("Edad ingresada no es válida")
                    else:
                        categoria = input("\tCategoria: ")
                        if categoria.lower() != "juvenil" and categoria.lower() != "adulto" and categoria.lower() != "master":
                            print("La categoria que ingresó no existe")
                        else:
                            participantes[dorsal] = {
                                "nombre": nombre,
                                "edad": edad,
                                "categoria": categoria,
                            }
                            dorsal += 1
                            print("Se agregó al particpante con éxito")
            case 2:
                if len(participantes) < 0:
                    print("No se ha agregado a ningún participante")
                    continue
    except ValueError:
        print("Dato ingresado no válido")