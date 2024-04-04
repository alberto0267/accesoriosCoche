AccesoriosDeCoche={
    "color": 50,
    "ventanas": 10,
    "llantas":20,
    "faros":10,
    "tuboEscape":10
}

auto =[]
colorAgregado=0
ventanasAgregado=0
llantasAgregado=0
farosAgregado=0
tuboEscapeAgregado=0

color=0
agregado=0
accesorioElegido = []
while True:
    print("-----------Menu--------------")
    print("1.Elige como quieres personalizar tu coche")
    print("2.Ver que le agregaste a tu coche")
    print("3.Total")
    print("4.Adios")
    opcion = input("elige un opcion: ")

    if opcion=="1":
        print("A personalizaaaaar!!!")
        for accesorios, accesorio in enumerate(AccesoriosDeCoche,start=1):
            print(accesorios, accesorio)



        seleccion = input("Elige el accesorio( y adios para salir): ")

        while seleccion.lower() != "adios":
          seleccion = int(seleccion)

          if seleccion in range(1,len(AccesoriosDeCoche)+1):
            accesorioElegido = list(AccesoriosDeCoche.keys())[seleccion-1]
            agregado+=1
            auto.append(accesorioElegido)
            if accesorioElegido == 'color' and colorAgregado <1:
                    colorAgregado += 1
                    print(f"{accesorioElegido} agregado ")

            elif accesorioElegido == "ventanas" and ventanasAgregado<=5:
                    ventanasAgregado += 1
                    print(f"{accesorioElegido} agregado ")
            elif accesorioElegido=="llantas" and llantasAgregado<=4:
                llantasAgregado+=1
                print(f"{accesorioElegido} agregado ")
            elif accesorioElegido == "faros" and farosAgregado<=2:
                farosAgregado+=1
                print(f"{accesorioElegido} agregado ")
            elif accesorioElegido == "tuboEscape" and tuboEscapeAgregado<=1:
                tuboEscapeAgregado+=1
                print(f"{accesorioElegido} agregado")
            else:
                if colorAgregado>1:
                     print("haz agregado mas de el color permitido")
                if ventanasAgregado >6:
                     print("haz agregado mas dee las ventanas permitidas")
                if  llantasAgregado>4:
                    print("haz agregado mas de las llantas permitidas")
                if farosAgregado >2:
                    print("haz agregado mas de los faros permitidos")
                if tuboEscapeAgregado > 1:
                    print("haz agregado mas de los tubos de escapes permitidos")
                else:
                    print("haz agregado algo de mas permitido, usa la logica")
          else:
             print("No existe")

          seleccion = input("Elige otro accesorio( y adios para salir): ")




    elif opcion == "2":
        print("Tus accesorios deportivos son: ")
        if agregado >=1:
            for accesorios1 in auto:
                print(accesorios1)
        else:
            print("Venga!!! no agregaste nada")

    elif opcion == "3":
        print("total de tus accesorios")
        if agregado >= 1:
            total = sum(AccesoriosDeCoche[accesorios1] for accesorios1 in auto)
            if total>=100:
                total=total*30/100
                print("el total es : ", "$ ", total)
                total="{:.2f}".format(total)
                print("tienes descuento del 30%")
                print("el total es : ", "$ ",total)
            else:
                print(f"el total es: ${total}")
        else:
            print("Venga!!! no agregaste nada")

    elif opcion == "4":
        print("Adios")
        break

    else:
        print("elige algo valido")



