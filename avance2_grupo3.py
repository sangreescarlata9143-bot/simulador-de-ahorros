opcion = ""
while opcion !="5":
    print("===== MENÚ SIMULADOR DE AHORROS =====")
    print("1. Incluir datos de ahorro")
    print("2. Consultar simulación")
    print("3. Modificar datos")
    print("4. Borrar datos")
    print("5. Salir")
    opcion = input("Seleccione una opción:")
    if opcion == "1":
        print("Elegiste incluir datos")
    elif opcion == "2":
        print("Elegiste consultar simulación")
    elif opcion == "3":
        print ("Elegiste modificar datos")
    elif opcion == "4":
        print("Elegiste borrar datos")
    elif opcion == "5":
        print("Saliendo del programa")
    else:
        print("Opción inválida")      