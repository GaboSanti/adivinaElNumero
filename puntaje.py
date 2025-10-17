'''
funcion del puntaje.
cada que el ususario adivine el numero en el input habra criterios a evaluar,
si el numero es igual al numero aleatario que hizo la funcion de numero aleatorio,
gana 100 puntos, si la diferiencia es de 1 a 9 gana 75 puntos,
si es de 10 a 19 gana 50 puntos,
si es de 20 a 39 gana 25 puntos,
y si es mas de 40 no gana puntos.
'''
from flask import Flask, jsonify, request
import json
import random

def puntaje(intento_entero):
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = intento_entero
    mensaje = ""
    
    if numero_usuario > numero_aleatorio:
        
        if numero_usuario == numero_aleatorio:
            mensaje= "acertaste"
            puntos = 100
        elif (numero_usuario - numero_aleatorio) <= 9:
            mensaje="quedaste muy cerca"
            puntos = 75
        elif (numero_usuario - numero_aleatorio) <= 19:
            mensaje="quedaste cerca"
            puntos = 50
        elif (numero_usuario - numero_aleatorio) <= 39:
            mensaje="lejos"
            puntos = 25
        else:
            mensaje="ni te acercaste"
            puntos = 0
    else:
        if numero_usuario == numero_aleatorio:
            mensaje= "acertaste"
            puntos = 100
        elif (numero_aleatorio - numero_usuario) <= 9:
            mensaje="quedaste muy cerca"
            puntos = 75
        elif (numero_aleatorio - numero_usuario) <= 19:
            mensaje="quedaste cerca"
            puntos = 50
        elif (numero_aleatorio - numero_usuario) <= 39:
            mensaje="lejos"
            puntos = 25
        else:
            mensaje="ni te acercaste"
            puntos = 0        
    
    return puntos,mensaje,numero_aleatorio