#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:04:57 2023

@author: darios
"""

#-------Tuplas-------------------

#crear una tupla con atajo
tupla_var=("manzana", "mango", "pera")
#Es diferente de una lista porque las listas se definen así:
lista_var=["manzana", "mango", "pera"]

#Es ordenada y no se puede cambiar después de crearse.

#Podemos preguntarle cuántos valores tiene:
print(len(tupla_var))

#Para preguntarle si es tupla usamos el comando: type()

#Podemos crear una tupla con un elemento
tupla_var=("valor1",)
print(type(tupla_var))

#Esto no es una tupla:
tupla_var=("valor1")
print(type(tupla_var))

#Las tuplas pueden ser de cualquier tipo: enteros, booleanos y Strings
#además podemos mezclar los tipos en las tuplas:
tupla_var=("String", 84, False)
print(type(tupla_var))

#Otra forma de crear una tupla es: 
tupla_nueva=tuple(("arbol", "casa", "perro"))
lista_nueva=list(("casa", "arbol", "perro"))
print(type(tupla_nueva))
print(type(lista_nueva))

#Para ver cada uno de los elementos.
print(tupla_nueva[0])

#Cuando mandamos a llamar un rango, me imprime de [0,2)
print(tupla_nueva[0:2])

#Podemos checar si existe algo en las tuplas, un valor que nosotros preguntemos.
if "casa" in tupla_nueva:
    print("Sí está casa en la tupla nueva")
    
    
#-------Para actualizar la tupla-----------
#Podemos cambiar la tupla si convertimos a lista y de regreso a tupla.
print(tupla_var)
y=list(tupla_var)
y[1]=139
tupla_var=tuple(y)
print(tupla_var)

#Usamos el mismo método para agregarle valores nuevos
print(tupla_var)
y=list(tupla_var)
y.append("Naranjas")
y.append(True)
tupla_var=tuple(y)
print(tupla_var)

#Idea: definir una función que haga estos cambios.
#Para quitar elementos se usa el mismo atajo.


#------desempacar la tupla-----------------
#definimos un vector de variables
(var1, var2, var3, var4, var5)=tupla_var
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)

#Podemos desempacar las variables en variables y además una lista.
(verde, azul, *rojo)=tupla_var
print(verde)
print(azul)
print(rojo)

(verde, *azul, rojo)=tupla_var
print(verde)
print(azul)
print(rojo)























