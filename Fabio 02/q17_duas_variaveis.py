from utils import obter_inteiro, escrever
def main():
    num1 = obter_inteiro('Digite o primeiro número: ')
    num2 = obter_inteiro('Digite o segundo número: ')

    opcoes = verificar_opcao(num1, num2)

    escrever(opcoes)


def verificar_opcao(n1, n2):
    if n1 % n2 == 1:
        operacao = n1 + n2 + n1 % n2
        return f'A soma dos números com o resto da divisão {operacao}'
    elif n1 % n2 == 2:
        eh_par = ''
        if n1 % 2 == 0 and n2 % 2 == 0:
            eh_par = 'Os dois números são pares'
        elif n1 % 2 == 0 and n2 % 2 != 0:
            eh_par = 'O primeiro número é par e o segundo é ímpar'
        elif n2 % 2 == 0 and n1 % 2 != 0:
            eh_par = 'O segundo número é par e o primeiro é ímpar'
        if n1 % 2 != 0 and n2 % 2 != 0:
            eh_par = 'Os dois números são ímpares'
        return eh_par
    elif n1 % n2 == 3:
        soma = n1 + n2
        multi = n1 * soma
        return f'A multiplicação da soma dos números pelo primeiro número resulta em {multi}'
    elif n1 % n2 == 4:
        soma = n1 + n2
        if n2 != 0:
            divisao = soma / n2
        return f'A divisão da soma dos números pelo segundo número resulta em {divisao}'
    else:
        q_n1 = n1 ** 2
        q_n2 = n2 ** 2
        return f'O quadrado dos números: o primeiro {q_n1} e o segundo {q_n2}'



main()   