
import os
import time

def contra(password):
    a = 1; b = 0
    s = 0; nuevopassword = ("")
    for letra in password:
        c = a + b
        a = b
        b = c
        if letra == "a":
            letra = "b"
            nuevopassword = nuevopassword + letra
            s = s + c
        elif letra == "b":
            letra = "c"
            nuevopassword = nuevopassword + letra
            s = s + c
        elif letra == "n":
            letra = "o"
            nuevopassword = nuevopassword + letra
            s = s + c
        elif letra == "e":
            letra = "h"
            nuevopassword = nuevopassword + letra
            s = s + c
        elif letra == "r":
            letra = "w"
            nuevopassword = nuevopassword + letra
            s = s + c
        else:
            return "None"
    if nuevopassword == "bcohw":
        if s == 12:
            return "Contraseña correcta"
def limpiarpantalla():
    time.sleep(2)
    os.system("cls")
    print("pantalla limpia")
def menu(entra):
    print("1. Primera operacion: Division de dos numeros")
    print("2. Segunda operacion: Divisores")
    print("3. Tercera operacion: Numeros capicua")
    print("4. Cuarta operacion: Cambio de base")
    print("5. salir")
    numero = int(input("¿Que operacion desea hacer? "))
    limpiarpantalla()
    print()
    if numero == 1:
        a = leer()
        b = leer()
        div, mod = divmod_1(a, b)
        print("la division es", div, "y el modulo", mod)
        limpiarpantalla()
        print()
        menu("entra")
    elif numero == 2:
        a = leer()
        while a <= 99999999999999:
            print("El numero debe ser mayor a 99999999999999")
            a = leer()
        b = 2
        print(1, end=" ")
        while b <= a:
            div, mod = divmod_1(a,b)
            b = b + 1
            if mod == 0:
                print(b, end=" ")
    elif numero == 3:
        a = leer()
        while a <= 99999999:
            print("El numero debe ser mayor a 99999999")
            a = leer()

    elif numero == 4:
        a = leer()
        b = leer()
        numerobinario = 0
        exponente = 0
        while a >= b:
            div, mod = divmod_1(a, b)
            numerobinario = numerobinario + mod * (10**exponente)
            exponente = exponente + 1
            a = div
        numerobinario = numerobinario + a * (10**exponente)
        print(numerobinario)
        limpiarpantalla()
        print()
        menu("entra")
    elif numero == 5:
        return
    else:
        print("Numero invalido")
        limpiarpantalla()
        print()
        menu("entra")
def divmod_1(a, b):
    div = 0
    while a >= b:
        a = a - b
        div = div + 1
    return div, a
def leer():
    n = int(input("ingrese un numero: "))
    return n
usuario = input("Usuario: ")
password = input("Contraseña: ")            #LA CONTRASEÑA ES: abner
nuevopassword = contra(password)
if nuevopassword == "Contraseña correcta":
    print(nuevopassword)
    limpiarpantalla()
    print()
    menu("entra")
    print("Finalizó el programa")
else:
    print(nuevopassword)