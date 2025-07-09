# Esta función recibe una lista de caracteres, un texto y un número de desplazamiento.
# Devuelve el texto cifrado utilizando el cifrado César.
def criptar_mensaje(lista, texto, numero):
    criptado = ''
    for caracter in texto:
        if caracter in lista:
            index = lista.index(caracter)
            desplazo = lista[(index + numero) % 26]
            criptado += desplazo
        else:
            criptado += caracter
    return criptado

# Esta función recibe una lista de caracteres y un mensaje cifrado.
# Intenta descifrar el mensaje utilizando un desplazamiento de 1 a 25.
def descifrar_criptado(lista ,mensaje):
    for i in range(25):
        descifrado = ''
        for caracter in mensaje:
            if caracter in lista:
                index = lista.index(caracter)
                desplazo = (index - i - 1) % 26
                descifrado += lista[desplazo]
            else:
                descifrado += caracter
        print(f'Intento {i+1}:\nPosible texto:\n{descifrado}\n')
