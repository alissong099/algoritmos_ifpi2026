from utils import escrever, obter_numero_real

def main():
    numero = obter_numero_real('Digite um número: ')

    resultado = inteiro_ou_decimal(numero)

    escrever(resultado)

def inteiro_ou_decimal(n):
    parte_fracionaria = n % 1

    if parte_fracionaria > 0 or parte_fracionaria < 0:
        return 'É um número decimal'
    else:
        return 'É um número inteiro'


main()