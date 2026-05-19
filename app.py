from convertidor import procesar_y_alinear_linea, LISTA_NOTAS
import pandas as pd
import json
import os

directorio = os.path.dirname(__file__)
ruta_json = os.path.join(directorio, "canciones.json")

def buscar_archivo_json(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f) 


def data_de_canciones():
    lista_canciones = {}
    data = buscar_archivo_json(ruta_json)
    
    for i in range(len(data)):
        opciones = data[i]['titulo']
        lista_canciones[i] = opciones
    return lista_canciones


def indices_canciones(repertorio):
    elegir_cancion = int(input("\nSeleccione el ID: ")) - 1
    if elegir_cancion in repertorio.keys():
        eleccion = (repertorio[elegir_cancion])
        print (f"\nCancion: {eleccion}")
        return elegir_cancion
    else:
        print ("Indice no localizado...")


def acceso_tonos(original, mi_key):
    # FILTRO
    if mi_key not in LISTA_NOTAS:
        print ("\nTonalidad no valida...")

    else:
        # CALCULO
        tono_base = LISTA_NOTAS.index(original)
        cambio_de_tono = LISTA_NOTAS.index(mi_key)

        calculo = cambio_de_tono - tono_base

        # RESPUESTA
        print (f"\n* CANCION ACTUALIZADA *")
        for verso in obtener_letra:
            respuesta = procesar_y_alinear_linea(verso, calculo)
            print (respuesta)


# SE MOSTRARA LAS CANCIONES DEL REPERTORIO
mi_repertorio = data_de_canciones()

print ("* CANCIONES DISPONIBLES *")
df = pd.DataFrame(mi_repertorio.values(), 
                  index=range(1, len( mi_repertorio.keys()) +1), 
                  columns=[" "])
print (df)

indice_seleccionado = indices_canciones(mi_repertorio)

acceso_data = buscar_archivo_json(ruta_json)
obtener_tono = acceso_data[indice_seleccionado]['tono_original']
obtener_letra = acceso_data[indice_seleccionado]['letra_con_acordes']

# SELECCIONAR TONALIDAD
key = input(f"Tono actual: {obtener_tono}\nCambiar a: ").upper()
acceso_tonos(obtener_tono, key)