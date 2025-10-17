from flask import Flask, jsonify, request, render_template, redirect, url_for
from puntaje import puntaje 

pedirnumero = Flask(__name__)

puntaje_total = 0 

@pedirnumero.route('/', methods=['GET'])
@pedirnumero.route('/numero', methods=['GET'])
def adivina_numero():
    """Muestra la página inicial del juego."""
    return render_template('index.html', mensaje=None,puntaje_actual=puntaje_total)
    
@pedirnumero.route('/adivinar', methods=['GET', 'POST'])
def procesar_intento():

    global puntaje_total 
    mensaje_respuesta = "" 
    
    if request.method == 'POST':
        
        valor_string = request.form.get('intento')
        
        if not valor_string:
             mensaje_respuesta = "Error: Por favor, ingresa un número."
        else:
            try:
                intento_entero = int(valor_string)
                
                puntos_ganados, mensaje_juego, numero_secreto  = puntaje(intento_entero)
                puntaje_total += puntos_ganados
        
                mensaje_respuesta = f"El número era {numero_secreto} <br> {mensaje_juego} <br> Ganaste {puntos_ganados} puntos. <br> Total acumulado: {puntaje_total}"

            except ValueError:
                mensaje_respuesta = "Error: Ingresa un número válido."
        
    else:
        return redirect(url_for('adivina_numero'))

    return render_template('index.html', mensaje=mensaje_respuesta) 


if __name__ == '__main__':
    pedirnumero.run(debug=True)