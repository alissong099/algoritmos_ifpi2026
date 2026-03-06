from utils import escrever, obter_inteiro

def main():
    numero = obter_inteiro('Digite um número de 4 digitos: ')

    resultado = verificar_quadrado_igual_a_numero(numero)

    escrever(resultado)

def verificar_quadrado_igual_a_numero(n):
    milhar = n // 1000
    resto = n % 1000
    centena = resto // 100

    primeria_dezena = milhar * 10 + centena
    segunda_dezena = resto % 100
    teceiro_numero = primeria_dezena + segunda_dezena

    quadrado_numero = teceiro_numero ** 2

    if quadrado_numero == n:
        return 'O número atende a caracteristica, a soma das dezenas do número elevado a 2 resulta no número'
    else:
        return 'O número não atende a caracteristica'


main() 