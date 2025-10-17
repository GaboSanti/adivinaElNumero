import json
import os
import uuid 

PUNTAJES_FILE = 'puntajes.json'

def guardar_puntaje_json(puntaje_final):
 # Función 5: Guardar puntajes con un ID   Autor:Isabel
    
    if os.path.exists(PUNTAJES_FILE) and os.path.getsize(PUNTAJES_FILE) > 0:
        with open(PUNTAJES_FILE, 'r') as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = []
    else:
        datos = []

    id_partida = str(uuid.uuid4()) 
    
    registro_nuevo = {
        'id': id_partida, 
        'puntaje': puntaje_final
    }
    
    datos.append(registro_nuevo)

    with open(PUNTAJES_FILE, 'w') as f:
        json.dump(datos, f, indent=4)
    return id_partida