# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:02:08 2021

@author: SERGIO
2do Examen INF - 319
Pregunta 1
"""
#Suma
def Suma(x, y):
    return x + y

# Resta
def Resta(x, y):
    return x-y
# Multiplica
def Multiplicar(x, y):
    return x * y

# División
def Dividdir(x, y):
    if(y==0):
        return "no hay division entre cero"
    else:
       return int(x / y) 

#calculadora
def calculadora(entrada,num1,num2):
    if entrada == '1':
        print("--La suma es: ",Suma(num1,num2))
    elif entrada == '2':
        print("--La Resta es: ",Resta(num1,num2))
    elif entrada == '3':
        print("--La Multiplicacion es: ",Multiplicar(num1,num2))
    elif entrada == '4':
        print("--La division es: ", Dividdir(num1,num2))
    else:
        print("ERROR numero incorrecto, intente de nuevo")

#Menu
while(True):
    print("******CALCULADORA EN PYTHON CON FUNCIONES******")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicar")
    print("4.Dividir")
    # Operación a realizar
    entrada = input("Que operacion desea realizar...digite (1/2/3/4): ")
    n1 = int(input("Primer número: "))
    n2 = int(input("segundo número: "))
    #Llamada a la funcion calculadora
    calculadora(entrada,n1,n2)



