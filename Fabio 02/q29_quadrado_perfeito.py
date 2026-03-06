from utils import obter_inteiro, escrever

def main():
    numero = obter_inteiro('Digite um número de 4 digitos: ')

    resultado = eh_quadrado_perfeito(numero)

    escrever(resultado)

def eh_quadrado_perfeito(n):
    raiz = n ** 0.5

    milhar = n // 1000
    resto = n % 1000
    centena = resto // 100

    segunda_dezena = resto % 100

    primeria_dezena = milhar * 10 + centena

    if raiz == (primeria_dezena + segunda_dezena):
        return 'É um quadrado perfeito'
    else:
        return 'Não é um quadrado perfeito'


main()