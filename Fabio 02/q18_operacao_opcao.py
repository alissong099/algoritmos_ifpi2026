from utils import escrever, obter_numero_real, obter_inteiro
def main():
    valor1 = obter_numero_real('Digite o primeiro valor: ')
    valor2 = obter_numero_real('Digite o segundo valor: ')

    opcoes = '''Escolha uma das opções a seguir:
(1) - Irá somar os valores
(2) - Irá subtrair os valores
(3) - Irá multiplicar os valores
(4) - Irá dividir os valores
Digite a opção que você quer: '''

    opcao = obter_inteiro(opcoes)

    operacao = realizar_operacao_escolhida(opcao, valor1, valor2)

    escrever(operacao)

def realizar_operacao_escolhida(opcao, v1, v2):
    if opcao == 1:
        soma = v1 + v2
        return f'A soma dos valores resulta em {soma}'
    elif opcao == 2:
        subtracao = v1 - v2
        return f'A subtração dos valores resulta em {subtracao}'
    elif opcao == 3:
        multi = v1 * v2
        return f'A multiplicação dos valores resulta em {multi}'
    elif opcao == 4:
        divisao = v1 / v2
        return f'A divisão dos valores resulta em {divisao}'
    else:
        return f'Opção inválida, por favor escolha uma das opções corretas'

main()