#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:46:44 2023

@author: darios
"""

#Listas

lista=[2,4,5]
lista=["Palabra", "Hola", "Camino"]

print(lista)

#Podemos pedirle a Python que nos regrese cualquier valor de la lista.

print(lista[0])

#Puede tener valores duplicados

lista=["Palabra", "Palabra", "Palabra"]

#Para regresar la longitud de la lista

print(len(lista))

#Permite que tengas diferentes tipos de valores

lista=[15, "Hola", True]

print(lista)

#Hay otra forma para declarar las listas

estaLista=list((4,3,2,23,4,4,2))

print(estaLista)


#Para trabajar con los elementos de las listas.

varaux=estaLista[0]*estaLista[1]
print(varaux)


varaux=estaLista[-1]*estaLista[-2]
print(varaux)


print(estaLista[:4])
print(estaLista[4:])


i=0
while(i<4):
    print(estaLista[i])
    i+=1


print(estaLista[:])
print(estaLista[-8:-1])



estaLista[2]="HOLA"
print(estaLista)

estaLista[4:7]=["Camino", "Perro", "Aire"]
print(estaLista)

estaLista[4:7]=["camino"]
print(estaLista)

#Comando insert
estaLista.insert(4, "buen")
print(estaLista)


#Append

estaLista.append(["Naranja", "Compra"])
print(estaLista)

#Para juntar 2 listas

otraLista=[False, True, True]

estaLista.extend(otraLista)
print(estaLista)

#Para quitar valores de la lista

#Nos quita todos los valores
estaLista.remove(4)
print(estaLista)


#Nos quita la posición que le pidamos, si no le decimos cual, nos quita la última
estaLista.pop()
print(estaLista)

estaLista.pop(5)
print(estaLista)

del estaLista[3]
print(estaLista)

#del estaLista
#print(estaLista)

#Limpia la lista por completo
#estaLista.clear()
#print(estaLista)

for x in estaLista:
    print(x)

for i in range(len(estaLista)):
    print(estaLista[i])

[print(x) for x in estaLista]


estaLista=["Hola", "Camino", "Hoy", "Mañana", "jueves"]
listavacia=[]
for x in estaLista:
    if "a" in x:
        listavacia.append(x)

print(listavacia)


listavacia=[x for x in estaLista if "a" in x]
print(listavacia)


#Sintaxis:
    #listanueva=[expresión for elemento in iterado if condición==true]


#Ejercicios:
#
#1. Pon la instrucción para que imprima el segundo elemento en la lista.
#   frutas=["manzana", "cereza", "agua"]
#   print(____)
#
#
#2. Agrega el elemento "naranja" a la lista
#   frutas=["manzana", "cereza", "agua"]
#
#
#3. Quita el elemento "cereza" de la lista
#   frutas=["manzana", "cereza", "agua", "naranja"]
#
#
#4. Usa el indexado negativo para imprimir el último elemento de la lista
#   frutas=["manzana", "cereza", "agua", "naranja"]
#   print(____)
#
#5. Imprime el tercer, cuarto y quinto elemento de la lista
#   frutas=["manzana", "cereza", "agua", "naranja", "kiwi"]
#   print(frutas(____))
#