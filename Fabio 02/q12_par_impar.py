from utils import obter_inteiro, escrever
def main():
    num = obter_inteiro('Digite um número para verificar se é par ou ímpar: ')

    verificar = eh_impar_ou_par(num)

    escrever(verificar)

def eh_impar_ou_par(n):
    if n % 2 == 0:
        return 'O número é par'
    else:
        return 'O número é ímpar'

main()  