import json

def recursiva(n):
    try:
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un entero.")
        if n < 0:
            raise ValueError("El número no puede ser negativo.")
        if n == 0:
            return "Done!"
        else:
            print(n)
            return recursiva(n - 1)
    except (TypeError, ValueError) as e:
        return f"Error capturado: {e}"


def fibonacci(n):
    try:
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un entero.")
        if n < 0:
            raise ValueError("Fibonacci no está definido para números negativos.")
            
        if (n == 0) or (n == 1):
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except (TypeError, ValueError) as e:
        return f"Error capturado: {e}"


def factorial(n):
    try:
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un entero.")
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
            
        if (n == 0) or (n == 1):
            return 1
        else:
            return factorial(n - 1) * n
    except (TypeError, ValueError) as e:
        return f"Error capturado: {e}"


def multiplicacion_recursiva(n, m):
    try:
        if not isinstance(n, int) or not isinstance(m, int):
            raise TypeError("Ambos valores deben ser enteros.")
        if m < 0:
            raise ValueError("El multiplicador (m) no puede ser negativo en esta implementación.")
            
        if m == 0:
            return 0
        else:
            return multiplicacion_recursiva(n, m - 1) + n
    except (TypeError, ValueError) as e:
        return f"Error capturado: {e}"


def division_entera_recursiva(dividendo, divisor):
    try:
        if not isinstance(dividendo, int) or not isinstance(divisor, int):
            raise TypeError("Los valores deben ser enteros.")
        if divisor == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        if dividendo < 0 or divisor < 0:
            raise ValueError("Esta implementación es solo para números positivos.")
            
        if dividendo - divisor < 0:
            return 0
        else:
            return division_entera_recursiva(dividendo - divisor, divisor) + 1
    except (TypeError, ValueError, ZeroDivisionError) as e:
        return f"Error capturado: {e}"


def potencia_recursiva(base, exponente):
    try:
        if not isinstance(exponente, int):
            raise TypeError("El exponente debe ser un entero.")
        if exponente < 0:
            raise ValueError("No se admiten exponentes negativos en esta versión.")
            
        if exponente == 0:
            return 1
        else:
            return potencia_recursiva(base, exponente - 1) * base
    except (TypeError, ValueError) as e:
        return f"Error capturado: {e}"


def serie_collatz(n):
    try:
        if not isinstance(n, int):
            raise TypeError("El valor debe ser un entero.")
        if n <= 0:
            raise ValueError("La serie de Collatz solo aplica para enteros positivos mayores a 0.")
            
        if n == 1:
            print("END!")
            return 0
        else:
            if n % 2 == 0:
                print(n // 2)
                return serie_collatz(n // 2)
            else:
                print(3 * n + 1)
                return serie_collatz(3 * n + 1)
    except (TypeError, ValueError) as e:
        return f"Error capturado: {e}"


def aplanar_json(diccionario, clave_padre='', separador='.'):
    try:
        if isinstance(diccionario, list):
            diccionario = dict(enumerate(diccionario)) [cite: 27]
            
        elementos = []
        for key, value in diccionario.items():
            # Forzar llave como texto 
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else str(key)
            
            if isinstance(value, dict):
                elementos.extend(aplanar_json(value, nueva_llave, separador).items()) [cite: 14]
            elif isinstance(value, list):
                # Diccionario
                dict_desde_lista = dict(enumerate(value)) [cite: 27]
                # Evitar iterar listas
                elementos.extend(aplanar_json(dict_desde_lista, nueva_llave, separador).items())
            else:
                elementos.append((nueva_llave, value))
                
        return dict(elementos)
    except AttributeError:
        return "Error: La función intentó leer una estructura no válida con .items()."
    except Exception as e:
        return f"Error inesperado al procesar JSON: {e}"

if __name__ == "__main__":
    print("--- Probando recursiva ---")
    print(recursiva(-3))   
    print(recursiva(5))   

    print("\n--- Probando division_entera_recursiva ---")
    print(division_entera_recursiva(10, 0)) 
    print(division_entera_recursiva(17, 5)) 

    print("\n--- Probando aplanar_json ---")
    json_prueba = {
        'alumnos':[
            {"Roman":"Hola"},
            {"Emiliano":"Hola mundo"},
            {"Nathan": "Esta muy bien"},
            {"Stephan":"Adios"},
            {"Materias": {"Programación": {"Unidad 1": 9, "Unidad 2": 8, "Unidad 3": 10}}}
        ]
    }
    
    # Aplanar salida 
    resultado_plano = aplanar_json(json_prueba)
    print(json.dumps(resultado_plano, indent=4, ensure_ascii=False))