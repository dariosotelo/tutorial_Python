#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:42:43 2023

@author: darios
"""

#------Diccionarios-------------------------

este_diccionario={
    "marca":"Ford",
    "modelo":"Mustang",
    "año":1964    
    }

#Para imprimir:
print(este_diccionario["marca"])


#No se puede tener dos llaves diferentes, como dos marcas, o dos años.
este_diccionario_esta_mal={
    "marca":"Ford",
    "modelo":"Mustang",
    "año":1964,
    "año":1970    
    }

#podemos preguntarle el tamaño del diccionario
print(len(este_diccionario))


este_diccionario={
    "marca":"Ford",
    "modelo":"Mustang",
    "año":1964,
    "colores":["rojo", "azul", "blanco", "verde"]    
    }


#Diccionario adentro de un diccionario
este_diccionario={
    "marca":"Ford",
    "modelo":"Mustang",
    "año":1964,
    "colores":{"rojo":"rojojijo", "azul":"cielo", "blanco":"grisosos", "verde":"ITAM"}    
    }


#Podemos declarar un diccionario dict()

#-----acceder elementos------------------------

colores=este_diccionario["colores"]["azul"]
print(colores)
#estas dos instrucciones son iguales
colores=este_diccionario.get("colores")
print(colores)

llaves=este_diccionario["colores"].keys()
print(llaves)



















































