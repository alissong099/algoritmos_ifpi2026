from utils import obter_numero_real,escrever

def main():
    numero = obter_numero_real('Digite um número qualquer: ')

    verificar = eh_positivo(numero)

    escrever(verificar)

def eh_positivo(n):
    if n == 0:
        return 'Número 0 não é positivo e nem negativo'
    if n < 0:
        return 'O número é negativo'
    else:
        return 'O número é positivo'

main()    