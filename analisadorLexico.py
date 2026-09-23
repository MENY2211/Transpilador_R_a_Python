import regex as re

especificacion_tokens = [
    ('COMENTARIO', r'#.*'),
    ('STRING', r'"([^"\\]|\\.)*"' + r"|'([^'\\]|\\.)*'"),
    ('DOUBLE', r'\d+(?:\.\d+)?'),

    ('PR_IF', r'\bif\b'),
    ('PR_ELSE', r'\belse\b'),
    ('PR_FOR', r'\bfor\b'),
    ('PR_IN', r'\bin\b'),
    ('PR_RETURN', r'\breturn\b'),
    ('PR_FUNCTION',       r'\bfunction\b'),

    ('PR_LENGTH', r'\blength(?=\()'),
    ('CONTENEDOR', r'\bc(?=\()'),
    ('FUNCION', r'[a-zA-Z]\w*(?=\()'),

    ('VARIABLE', r'[a-zA-Z]\w*'),

    ('SB_MENOR_IGUAL', r'<='),
    ('SB_MAYOR_IGUAL', r'>='),
    ('SB_IGUALDAD', r'=='),
    ('SB_DIFERENTE', r'!='),
    ('SB_MENOR_QUE', r'<'),
    ('SB_MAYOR_QUE', r'>'),

    ('SB_ASIGNACION', r'='),

    ('OP_SUMA', r'\+'),
    ('OP_RESTA', r'-'),
    ('OP_MULT', r'\*'),
    ('OP_DIV', r'/'),
    ('OP_DOS_PUNTOS',  r':'),  

    ('PARENTESIS_IZQ', r'\('),
    ('PARENTESIS_DER', r'\)'),
    ('LLAVE_IZQ', r'\{'),
    ('LLAVE_DER', r'\}'),
    ('CORCHETE_IZQ',   r'\['),
    ('CORCHETE_DER',   r'\]'),
    ('SEPARADOR', r','),

    ('SALTO_LINEA', r'\n'),
    ('ESPACIO', r'[ \t]+'),

    ('DESCONOCIDO', r'.'),
]


lista_patrones = []
for tupla in especificacion_tokens:
    nombre = tupla[0]
    patron = tupla[1]
    grupo_nombrado = "(?P<" + nombre + ">" + patron + ")"
    lista_patrones.append(grupo_nombrado)

patron_maestro = ""
es_primer_elemento = True

for elemento in lista_patrones:
    if es_primer_elemento:
        patron_maestro = elemento
        es_primer_elemento = False
    else:
        patron_maestro = patron_maestro + "|" + elemento


def tokenizar(codigo):
    tokens = []
    linea_actual = 1

    for coincidencia in re.finditer(patron_maestro, codigo):
        familia = coincidencia.lastgroup

        lexema = coincidencia.group()

        if familia == 'SALTO_LINEA':
            linea_actual = linea_actual + 1
            continue

        if familia == 'ESPACIO':
            continue

        if familia == 'COMENTARIO':
            continue

        if familia == 'DESCONOCIDO':
            mensaje_error = "Error léxico: Carácter extraño no permitido '" + lexema + "' encontrado en la línea " + str(linea_actual) + ". Análisis cancelado."
            raise ValueError(mensaje_error)

        # Si el token es válido, se construye la tupla explícitamente y se agrega
        token_actual = (familia, lexema, linea_actual)
        tokens.append(token_actual)

    return tokens


def analizar_archivo(ruta_archivo):
    """
    Abre el archivo de texto indicado, lo lee completo, y
    manda su contenido a la función tokenizar().
    """
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    codigo = archivo.read()
    archivo.close()

    resultado_tokens = tokenizar(codigo)
    return resultado_tokens

if __name__ == '__main__':
    try:
        lista_de_tokens = analizar_archivo('prueba.txt')

        for token in lista_de_tokens:
            familia = token[0]
            lexema = token[1]
            linea = token[2]
            
            # Formato de salida explícito alineado con espacios sobrantes
            familia_alineada = familia.ljust(15)
            linea_str = str(linea).rjust(3)
            
            print("Línea " + linea_str + "  " + familia_alineada + "  " + repr(lexema))

    except ValueError as error:
        print(error)