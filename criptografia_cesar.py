def criptografar_cesar(mensagem, deslocamento):
    mensagem_criptografada = ""
    for caractere in mensagem:
        if caractere.isupper():
            novo_caractere = chr((ord(caractere) - 65 + deslocamento) % 26 + 65)
            mensagem_criptografada += novo_caractere
        elif caractere.islower():
            novo_caractere = chr((ord(caractere) - 97 + deslocamento) % 26 + 97)
            mensagem_criptografada += novo_caractere
        else:
            mensagem_criptografada += caractere
    return mensagem_criptografada

def descriptografar_cesar(mensagem_criptografada, deslocamento):
    mensagem_descriptografada = ""
    for caractere in mensagem_criptografada:
        if caractere.isupper():
            novo_caractere = chr((ord(caractere) - 65 - deslocamento) % 26 + 65)
            mensagem_descriptografada += novo_caractere
        elif caractere.islower():
            novo_caractere = chr((ord(caractere) - 97 - deslocamento) % 26 + 97)
            mensagem_descriptografada += novo_caractere
        else:
            mensagem_descriptografada += caractere
    return mensagem_descriptografada

mensagem = input("Digite a mensagem a ser criptografada: ")
deslocamento = int(input("Digite o deslocamento: "))

mensagem_criptografada = criptografar_cesar(mensagem, deslocamento)
print("Mensagem criptografada:", mensagem_criptografada)

mensagem_descriptografada = descriptografar_cesar(mensagem_criptografada, deslocamento)
print("Mensagem descriptografada:", mensagem_descriptografada)