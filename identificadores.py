class Tokens:
    def __init__(self):
        self.familia_patron = [
            ('COMENTARIO', r'#.*'),
            ('STRING', r'(?:"[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\')'),
            ('DOUBLE', r'\d+(?:\.\d+)?'),

            ('PR_IF', r'\bif\b'),
            ('PR_ELSE', r'\belse\b'),
            ('PR_FOR', r'\bfor\b'),
            ('PR_IN', r'\bin\b'),
            ('PR_RETURN', r'\breturn\b'),
            ('PR_FUNCTION', r'\bfunction\b'),
            ('PR_PRINT', r'\bprint(?=\()'),
            ('PR_LENGTH', r'\blength(?=\()'),

            ('CONTENEDOR', r'\bc(?=\()'),
            ('FUNCION', r'[a-zA-Z_]\w*(?=\()'),

            ('VARIABLE', r'[a-zA-Z_]\w*'),

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
            ('OP_DOS_PUNTOS', r':'),  

            ('PARENTESIS_IZQ', r'\('),
            ('PARENTESIS_DER', r'\)'),
            ('LLAVE_IZQ', r'\{'),
            ('LLAVE_DER', r'\}'),
            ('CORCHETE_IZQ', r'\['),
            ('CORCHETE_DER', r'\]'),
            ('SEPARADOR', r','),

            ('SALTO_LINEA', r'\n'),
            ('ESPACIO', r'[ \t]+'),
            ('COMILLA_S', r'\''),
            ('COMILLA_D', r'\"'),
            ('PUNTO', r'\.'),
            ('PUNTO', r'\.'),

            ('DESCONOCIDO', r'.'),
        ]

    def obtenerPatronMaestro(self):
        lista_patrones = []

        for i in self.familia_patron:
            familia = i[0]
            patron= i[1]
            grupo_nombrado = "(?P<" + familia + ">" + patron + ")"
            lista_patrones.append(grupo_nombrado)
            "print(lista_patrones)"

        reglas_lexicas = ""
        es_primer_elemento = True

        for i in lista_patrones:
            if es_primer_elemento:
                reglas_lexicas = i
                es_primer_elemento = False
                "print(patron)"
            else:
                reglas_lexicas = reglas_lexicas +"|"+ i
        "print(reglas_lexicas)"
        return reglas_lexicas