
import numpy
from colorama import Style, Fore
import msvcrt
import random
import os

###########################################
#CREAR ARREGLO

libros=numpy.empty([10,4], object)

###########################################
#FUNCIONES DE DISEÑO

def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def limpiarpantalla():
    printv("<<Preseone una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

###########################################
#FUNCIONES DE ARREGLO

#VALIDAR
def validarC (cod):
    for i in range (10):
        if libros [i,0]==cod:
            return i
    return-1

#GUARDAR
def guardar (cod,titulo,autor,presio):
    if None in libros:
        if validarC(cod)==-1:
            if presio>0:
                for i in range(10):
                    if libros[i,0]==None:
                            libros[i,0]==cod
                            libros[i,1]==titulo
                            libros[i,2]==autor
                            libros[i,3]==presio
                            printv("Libro registrado")
                            break
            else: 
                printr ("El presio debe de ser mayor a 0")
        else:
            printr("Codigo repetido")
    else:
        printr("No hay espacio")

#BUSCAR


#CERTIFICADO1
critica=[]
critica.append("Muy buen libro")
critica.append("No entendí nada")
critica.append("aburrido")
critica.append("increible historia")
critica.append("no lo recomiendo")
critica.append("Extraño pero bueno")
critica.append("mogege")
critica.append("AAAAAAAAAAAAAAAAAAA")
critica.append("una patata es mas interesante")
critica.append("BUENISIMOOOO")

def critica(codigo):
    posicion=validarC(codigo)
    if posicion>=0:
        print(f"""
        --------------------------------------------
        Certificado Critica de {libros[posicion,1]}
        --------------------------------------------
        CODIGO: {libros[posicion,0]}
        --------------------------------------------
        1) {critica[random.randint(0,9)]}
        2) {critica[random.randint(0,9)]}
        3) {critica[random.randint(0,9)]}
        --------------------------------------------
        """)

#CERTIFICADO2
