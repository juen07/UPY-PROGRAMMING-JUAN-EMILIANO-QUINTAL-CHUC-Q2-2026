class DigitoApocrifoError(Exception):
    pass

try:
    rol = input("Escribe el rol: ")
    rol_sin_digito, digito = rol.split("-")
    check = False

except ValueError:
    print("Rol inválido: No tiene el formati xxxxxxxxx-x")

else:
    try:
        digito = int(digito)
    except ValueError:
        print("El digito verificador deber ser un número")
    else:
        try:
            inverso = [int(i) for i in rol_sin_digito]

        except ValueError:
            print("Los digitos deben ser númericos")

        else:
            inverso = inverso[::-1]
            secuencia = [2,3,4,5,6,7]
            suma = 0

            for index in range (len(inverso)):
                numero = inverso[index]
                suma +=  numero * secuencia[index % 6]

            resultado = suma % 11
            verificador = 11 - resultado

            try:
                if verificador != int(digito):
                    raise DigitoApocrifoError()

            except DigitoApocrifoError as e:
                print("Digito verificador apocrifo")

            print(f"{rol_sin_digito} - {verificador}")