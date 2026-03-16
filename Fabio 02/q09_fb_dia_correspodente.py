from utils import obter_inteiro, escrever

def main():
    numero = (obter_inteiro('Digite um número de 1 a 7: '))

    dia = definir_dia(numero)

    escrever(dia)

def definir_dia(n):
    if n == 1:
        return '1-Domingo'
    elif n == 2:
        return '2-Segunda'
    elif n == 3:
        return '3-Terça Feira'
    elif n == 4:
        return '4-Quarta Feira'
    elif n == 5:
        return '5-Quinta Feira'
    elif n == 6:
        return '6-Sexta Feira'
    elif n == 7:
        return '7-Sábado'
    else:
        return 'Digite um número válido'


main()