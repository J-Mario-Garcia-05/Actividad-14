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

participantes = []
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
                if cantidad < 1 or cantidad > 10:
                    print("La cantidad debe estar entre 1 y 10")
                    continue
                for i in range(cantidad):
                    print(f"Datos del participante {i + 1}:")
                    nombre = input("\tNombre completo: ")
                    edad = int(input("\tEdad: "))
                    if edad < 10 or edad > 60:
                        print("Edad ingresada no es válida")
                    else:
                        categoria = input("\tCategoria: ").lower()
                        if categoria not in ["juvenil", "adulto", "master"]:
                            print("La categoria que ingresó no existe")
                        else:
                            participantes.append({
                                "dorsal": dorsal,
                                "nombre": nombre,
                                "edad": edad,
                                "categoria": categoria,
                            })
                            dorsal += 1
                            print("Se agregó al particpante correctamente")
            case 2:
                if not participantes:
                    print("No se ha agregado a ningún participante")
                    continue
                print("\nParticpantes ordenados por nombre:")
                for i in ordenar_nombre(participantes):
                    print(f"{i['nombre']}: (dorsal:{i['dorsal']} edad: {i['edad']}, categoría: {i['categoria']}")
            case 3:
                if not participantes:
                    print("No se ha agregado a ningún participante")
                    continue
                print("participantes ordenados por edad:")
                for i in ordenar_edad(participantes):
                    print(f"{i['nombre']}: (dorsal:{i['dorsla']} edad: {i['edad']}, categoría: {i['categoria']}")
            case 4:
                print("Saliendo")
            case __:
                print("Opción no disponible")
    except ValueError:
        print("Dato ingresado no válido")