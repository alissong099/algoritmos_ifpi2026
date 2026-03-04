from utils import obter_inteiro, escrever
def main():
    num1 = obter_inteiro('Digite o primeiro número: ')
    num2 = obter_inteiro('Digite o segundo número: ')
    num3 = obter_inteiro('Digite o terceiro número: ')

    opcoes = '''Escolha uma das opções a seguir:
(1) - Irá mostrar o primeiro número
(2) - Irá mostar o segundo número
(3) - Irá mostar o terceiro número
Digite a opção que você quer: '''

    opcao = obter_inteiro(opcoes)

    escolha = verificar_opcao_escolhida(opcao, num1, num2, num3)

    escrever(escolha)

def verificar_opcao_escolhida(opcao, n1, n2, n3):
    if opcao == 1:
        return f'Aqui está o primereiro número {n1}'
    elif opcao == 2:
        return f'Aqui está o segundo número {n2}'
    elif opcao == 3:
        return f'Aqui está o terceiro número {n3}'
    else:
        return 'A opção é inválida. Por favor escolha uma das opções corretas.'

main()    