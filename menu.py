from main import criptar_mensaje, descifrar_criptado
from os import system

print("Bienvenido al programa de cifrado César")
def menu():
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opción no válida. Elija una de las opciones.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def inicio():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        opcion = menu()
        if opcion == 1:
            system('cls')
            texto = input('Ingrese el texto a cifrar: ').lower()
            desplazamiento = int(input('Ingrese el número de desplazamiento: '))
            mensaje_cifrado = criptar_mensaje(abc, texto, desplazamiento)
            print(f'Mensaje cifrado: {mensaje_cifrado}')
        elif opcion == 2:
            system('cls')
            mensaje_cifrado = input('Ingrese el mensaje cifrado: ').lower()
            descifrar_criptado(abc, mensaje_cifrado)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            
        input("Presione Enter para continuar...")
        system('cls')
        
        
if __name__ == "__main__":
    inicio()