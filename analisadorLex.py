import regex as re
from identificadores import *

tokens = Tokens()
familia_patron = tokens.familia_patron
reglas_lexicas = tokens.obtenerPatronMaestro()


def tokenizar(codigo, reglas_lexicas, familia_patron):
    tokens = []
    linea_actual = 1
    posicion = 0
    limite_codigo = len(codigo)

    patron = re.compile(reglas_lexicas)

    while posicion < limite_codigo:
        coincidencia = patron.match(codigo, posicion)
        'print(coincidencia)'
        if not coincidencia:
            caracter_malo = codigo[posicion]
            mensaje_error = f"Error léxico: Carácter no permitido '{caracter_malo}' en la línea {linea_actual}."
            raise ValueError(mensaje_error)

        familia = coincidencia.lastgroup
        lexema = coincidencia.group()

        posicion = coincidencia.end()

        if familia == 'SALTO_LINEA':
            linea_actual += 1
            continue

        if familia == 'ESPACIO':
            continue

        if familia == 'DESCONOCIDO':
            mensaje_error = f"Error léxico: Carácter no permitido '{lexema}' en la línea {linea_actual}."
            raise ValueError(mensaje_error)

        tokens.append((familia, lexema, linea_actual))
    return tokens

def analizar_archivo(ruta_archivo, reglas_lexicas, familia_patron):
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    codigo = archivo.read()
    archivo.close()

    resultado_tokens = tokenizar(codigo, reglas_lexicas, familia_patron)

    return resultado_tokens

try:
    lista_de_tokens = analizar_archivo('prueba.txt',reglas_lexicas, familia_patron)
    print('\n')
    for token in lista_de_tokens:
        familia = token[0]
        lexema = token[1]
        linea = token[2]
            
        familia_alineada = familia.ljust(15)
            
        print(str(linea) + '  ' + familia_alineada + "  " + repr(lexema))
    print('\n')

except ValueError as error:
    print(error)


