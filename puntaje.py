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

def puntaje():
    numero_aleatorio = random.randint(1, 100)
    datos = request.get_json()
    numero_usuario = datos.get('numero_usuario')
    
    if numero_usuario > numero_aleatorio:
        
        if numero_usuario == numero_aleatorio:
            print("acertaste")
            puntos = 100
        elif (numero_usuario - numero_aleatorio) <= 9:
            print("quedaste muy cerca")
            puntos = 75
        elif (numero_usuario - numero_aleatorio) <= 19:
            print("quedaste cerca")
            puntos = 50
        elif (numero_usuario - numero_aleatorio) <= 39:
            print("lejos")
            puntos = 25
        else:
            print("ni te acercaste")
            puntos = 0
    else:
        if numero_usuario == numero_aleatorio:
            print("acertaste")
            puntos = 100
        elif (numero_aleatorio - numero_usuario) <= 9:
            print("quedaste muy cerca")
            puntos = 75
        elif (numero_aleatorio - numero_usuario) <= 19:
            print("quedaste cerca")
            puntos = 50
        elif (numero_aleatorio - numero_usuario) <= 39:
            print("quedaste cerca")
            puntos = 25
        else:
            print("ni te acercaste")
            puntos = 0        
    
    return puntos