from flask import Flask, jsonify, request, render_template
from generarNumero import generar_numero
pedirnumero = Flask(__name__, template_folder='.')



# puntajeParcial = 

@pedirnumero.route('/', methods=['GET', 'POST'])
def adivina_numero():
    
    return render_template('index.html')
        
        
        
        


if __name__ == '__main__':
    pedirnumero.run(debug=True)
    
    
    