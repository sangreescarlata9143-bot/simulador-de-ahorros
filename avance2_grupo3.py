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
        nombre = input("¿motivo del ahorro? ")
        monto = float(input("¿Cuánto dinero tienes ahorrado? $"))
        ahorros.append(nombre + ": $" + str(monto))
        print("Elegiste incluir datos")
    elif opcion == "2":
         if len(ahorros) == 0:
            print("No tienes ahorros registrados.")
        else:
            print("\nTus ahorros:")
            for i in range(len(ahorros)):
                print(str(i+1) + ". " + ahorros[i])
        print("Elegiste consultar simulación")
    elif opcion == "3":
  if len(ahorros) == 0:
            print("No datos para eliminar.")
        else:
            for i in range(len(ahorros)):
                print(str(i+1) + ". " + ahorros[i])
            numero = int(input("¿Cuál quieres borrar? "))
            ahorros.pop(numero - 1)
            print("Borrado exitosamente")
        print ("Elegiste modificar datos")
    elif opcion == "4":
  total = 0
        for item in ahorros:
            monto = float(item.split("$")[1])
            total = total + monto
        print("Total ahorrado: $" + str(total))
        print("Elegiste borrar datos")
    elif opcion == "5":
        print("Saliendo del programa")
    else:
        print("Opción inválida")      
