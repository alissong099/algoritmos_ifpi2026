from utils import obter_inteiro, escrever
def main():
    horas1 = obter_inteiro('Informe a quantia de horas aula do professor 1: ')
    valor_hora1 = obter_inteiro('Informe o valor da hora do professor 1: ')
    horas2 = obter_inteiro('Informe a quantia de horas aula do professor 2: ')
    valor_hora2 = obter_inteiro('Informe o valor da hora do professor 2: ')

    maior_sal = verificar_maior_sal(horas1, valor_hora1, horas2, valor_hora2)

    escrever(maior_sal)

def verificar_maior_sal(h1, v1, h2, v2):
    sal1 = h1 * v1
    sal2 = h2 * v2
    if sal1 > sal2:
        return f'O professor 1 recebe um salário maior de R${sal1:.2f} e o salário do professor 2 é R${sal2:.2f}'
    elif sal1 == sal2:
        return f'Os professores tem um salário igual, salário do professor 1 R${sal1:.2f} e do professor 2 R${sal2:.2f}'
    else:
        return f'O professor 2 recebe um salário maior de R${sal2:.2f} e o salário do professor 1 é R${sal1:.2f}'


main()    