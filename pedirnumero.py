from flask import Flask, jsonify, request, render_template, redirect, url_for
from puntaje import puntaje 
from Guardar_Puntajes import guardar_puntaje_json
pedirnumero = Flask(__name__)

puntaje_total = 0
intentos = 0

@pedirnumero.route('/', methods=['GET'])
@pedirnumero.route('/numero', methods=['GET'])
def adivina_numero():# Función 1: Inicia el Juego Autor: Mario

    """Muestra la página inicial del juego."""
    return render_template('index.html', mensaje=None,puntaje_actual=puntaje_total)
    
@pedirnumero.route('/adivinar', methods=['GET', 'POST'])
def procesar_intento():# Función 4: Conversion de numero, llamado de funciones  Autor: Mario, Isabel

    global puntaje_total 
    global intentos
    mensaje_respuesta = "" 
    
    if request.method == 'POST':
        
        valor_string = request.form.get('intento')
        
        if not valor_string:
             mensaje_respuesta = "Error: Por favor, ingresa un número."
        elif valor_string.lower() == 'terminar':
            
            puntaje_guardado = puntaje_total
            
            id_partida = guardar_puntaje_json(puntaje_guardado) 
            
            # Reiniciar puntaje
            puntaje_total = 0 
            
            mensaje_respuesta = (f" Juego Terminado. <br>Tu puntaje de **{puntaje_guardado}** fue guardado.<br>"
                                 f"ID de partida: **{id_partida}**.<br>"
                                 f"Numero de intentos: **{intentos}**.<br>"
                                 f"¡Empieza de nuevo!")
        
        else:
            try:
                intento_entero = int(valor_string)
                
                puntos_ganados, mensaje_juego, numero_secreto  = puntaje(intento_entero)
                puntaje_total += puntos_ganados
                intentos+=1
        
                mensaje_respuesta = f"El número era {numero_secreto} <br> {mensaje_juego} <br> Ganaste {puntos_ganados} puntos. <br> Total acumulado: {puntaje_total} <br> Numero de juegos: {intentos}"

            except ValueError:
                mensaje_respuesta = "Error: Ingresa un número válido."
        
    else:
        return redirect(url_for('adivina_numero'))

    return render_template('index.html', mensaje=mensaje_respuesta) 


if __name__ == '__main__':
    pedirnumero.run(debug=True)