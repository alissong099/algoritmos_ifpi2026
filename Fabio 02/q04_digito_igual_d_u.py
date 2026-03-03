from utils import obter_inteiro, escrever
def main():
    numero = obter_inteiro("Digite um número de dois digitos: ")

    digito = eh_igual(numero)

    escrever(digito)

def eh_igual(numero):
    if numero // 10 == numero % 10:
        return "Os digitos são iguais"
    else:
        return 'Os digitos são diferentes'

main()    