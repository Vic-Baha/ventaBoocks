import ventaboocks as fu

while True:
    fu.limpiarpantalla()
    fu.printv("SISTEMA VENTABOOCKS")
    fu.printv("*******************")
    print("1) Guardar")
    print("2) Buscar")
    print("3) Certificado")
    print("0) SALIR")
    opcion=int(input("Seleccione: "))

    #validamos la opcion
    if opcion==0:
        fu.printv("Adios :D")
        break
    elif opcion==1:
        fu.printv("Guardar")
    elif opcion==2:
        fu.printv("Buscar")
    elif opcion==3:
        fu.printv("Certificado")
        print("1) Criticas del libro ")
        print("2) Detalle de ventas ")
        opcicer=int(input("Seleccione: "))
        if opcicer==1:
            fu.printv("<<Criticas>>")
        elif opcicer==2:
            fu.printv("<<Detalle Venta>>")
        else:
            fu.printr ("Opcion no valida")
    else:
        fu.printr("Opcion no valida")