
from flask import Flask, jsonify, request, render_template, redirect, url_for

from puntaje import puntaje 

pedirnumero = Flask(__name__)


NUMERO_SECRETO = 42 

@pedirnumero.route('/', methods=['GET'])
@pedirnumero.route('/numero', methods=['GET'])
def adivina_numero():
    """Muestra la página inicial del juego."""
    return render_template('index.html', mensaje=None)
    
@pedirnumero.route('/adivinar', methods=['GET', 'POST'])
def procesar_intento():
    
    mensaje_respuesta = "" 
    
    if request.method == 'POST':
        
        valor_string = request.form.get('intento')
        print(f"Valor recibido del formulario: {valor_string}")
        
        if not valor_string:
             mensaje_respuesta = "Error: Por favor, ingresa un número."
        else:
            try:
                intento_entero = int(valor_string)
                print(f"Número capturado por Python (Entero): {intento_entero}")
                
                puntos_obtenidos = puntaje(intento_entero)
                
                
                mensaje_respuesta = f"Puntos:{puntos_obtenidos}"

            except ValueError:
                mensaje_respuesta = "Error: Ingresa un número válido."
        
    else:
        return redirect(url_for('adivina_numero'))

    return render_template('index.html', mensaje=mensaje_respuesta) 


if __name__ == '__main__':
    pedirnumero.run(debug=True)
