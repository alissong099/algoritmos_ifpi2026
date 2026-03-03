from utils import escrever, obter_numero_real
def main():
    num1 = obter_numero_real("Digite o primeiro número: ")
    num2 = obter_numero_real("Digite o segundo número: ")
    num3 = obter_numero_real("Digite o terceiro número: ")

    numeros = [num1, num2, num3]
    contagem_iguais = 0

    if num1 == num2 and num2 == num3:
        escrever("Existem 3 números iguais.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        escrever("Existem 2 números iguais.")
    else:
        escrever("Existem 0 números iguais.")

main()
