from utils import escrever, obter_inteiro

def main():
    x1 = obter_inteiro('Digite o valor do X do ponto 1: ')
    y1 = obter_inteiro('Digite o valor do Y do ponto 1: ')
    x2 = obter_inteiro('Digite o valor do X do ponto 2: ')
    y2 = obter_inteiro('Digite o valor do Y do ponto 2: ')

    area = obter_area_retangulo(x1, y1, x2, y2)

    escrever(area)

def obter_area_retangulo(x1, y1, x2, y2):
    base = x2 - x1
    altura = y2 - y1
    if base < 0:
        base = base * -1
    if altura < 0:
        altura = altura * -1
    area = base * altura
    return f'A área do retangulo é  de {area}'

main()    