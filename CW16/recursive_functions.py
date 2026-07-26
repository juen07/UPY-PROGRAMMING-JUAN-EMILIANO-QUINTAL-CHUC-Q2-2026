def fibonnaci(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return factorial(n - 1) * n

def multiplicacion_recursiva(n, m):
    if m == 0:
        return 0
    else:
        return multiplicacion_recursiva(n, m - 1) + n
    
def division_entera_recursiva(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return division_entera_recursiva(dividendo - divisor, divisor) + 1

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return potencia_recursiva(base, exponente - 1) * base

def serie_collatz(n):
    if n == 1:
        return "END"
    else:
        if n % 2 == 0:
            print(n / 2)
            return serie_collatz(n / 2)
        else:
            print(3 * n + 1)
            return serie_collatz(3 * n + 1)


def aplanar_json(diccionario, clave_padre = '', separador = '.'):
    elementos = []
    for key, value in diccionario.items():
        nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
        if isinstance(value, dict):
            elementos.extend(aplanar_json(value, nueva_llave, separador).items())
        else:
            elementos.append((nueva_llave, value))
    return dict(elementos)


#print(serie_collatz(4))
json_prueba = {
    'alumnos' : [{"Roman": "Hola"},
                 {"Emiliano": "Hola mundo"}, 
                 {"Nathan": "Esta Muy Bien"}, 
                 {"Stephan": "Adios"},
                 {'Materias': {"Programacion": {"Unidad 1": 9, "Unidad 2": 8, "Unidad 3": 10}}}
    ]
}

print(aplanar_json(json_prueba))