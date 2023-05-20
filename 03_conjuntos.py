#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:25:22 2023

@author: darios
"""

#------Conjuntos-------------------------

#las listas se declaran:
lista=[1,2,3]

#las tuplas se declaran:
tupla=(1,2,3)

#los conjuntos se declaran:
primer_conjunto={"manzana", "pera", "perro", True, 1, True, 0, False, 10}

#1 y True son el mismo elemento
print(primer_conjunto)

#Podemos ver la longitud de un conjunto
print(len(primer_conjunto))

#Podemos pasar de conjunto a lista con el comando list()
guarda_lista=list(primer_conjunto)

#Podemos preguntar de qué tipo es una estructura de datos
print(type(primer_conjunto))
print(type(guarda_lista))

#Una forma más formal de declarar los conjuntos es:
este_conjunto=set(("las", "cosas"))

#Podemos acceder a los elementos de los conjuntos
print("manzana" in primer_conjunto)


#------agregar elementos-------------------
primer_conjunto.add("Martes")
print(primer_conjunto)


#podemos agregar varios elementos a la vez
segundo_conjunto={"lunes", "viernes", "jueves"}

primer_conjunto.update(segundo_conjunto)

print(primer_conjunto)

#segundo_conjunto puede ser de cualquier tipo, lista, tupla o diccionario.

#-----quitar elementos---------------------

#si usando remove(elemento) "elemento" no existe, va a regresar un error
primer_conjunto.remove("Martes")

print(primer_conjunto)

#usando discard, hace que no quiebre el código
primer_conjunto.discard("semana")

print(primer_conjunto)
























