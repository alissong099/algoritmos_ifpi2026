from utils import escrever, obter_texto

def main():
    letra = obter_texto('Digite uma letra do alfabeto: ')

    verificar = vogal_ou_consoante(letra)

    escrever(verificar)

def vogal_ou_consoante(l):
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        return 'A letra é uma vogal'
    else:
        return 'A letra é uma consoante'


main()