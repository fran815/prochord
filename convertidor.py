import re

LISTA_NOTAS = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def separar_acorde(acorde):
    if len(acorde) > 1 and acorde[1] == '#': # SE BUSCA EL TONO RAIZ EN EL COMPLEJO
        raiz = acorde[:2]
        extension = acorde[2:]
    else: # TOMA EL TONO SIMPLE 
        raiz = acorde[:1]
        extension = acorde[1:]
    return raiz, extension


def transportar_acorde_individual(acorde, semitonos):
    raiz, extension = separar_acorde(acorde)
    encontrar_indice = LISTA_NOTAS.index(raiz)
    nuevo_indice = (encontrar_indice + semitonos) % len(LISTA_NOTAS)
    return LISTA_NOTAS[nuevo_indice] + extension


def procesar_y_alinear_linea(mi_cancion, semitonos):
    linea_acordes = ""
    linea_texto = ""
    ultimo_indice_texto = 0

    for coincidencia in re.finditer(r'\[(.*?)\]', mi_cancion):
        acorde_original = coincidencia.group(1)
        inicio_bloque, fin_bloque = coincidencia.span()
        
        # TRANSPORTAR TONOS
        acorde_transportado = transportar_acorde_individual(acorde_original, semitonos)
        texto_previo = mi_cancion[ultimo_indice_texto:inicio_bloque]
        linea_texto += texto_previo

        linea_acordes += " " * (len(linea_texto) - len(linea_acordes))
        linea_acordes += acorde_transportado

        ultimo_indice_texto = fin_bloque
    
    linea_texto += mi_cancion[ultimo_indice_texto:]
    
    if not linea_acordes.strip():
        return linea_texto
    
    return f"{linea_acordes}\n{linea_texto}"