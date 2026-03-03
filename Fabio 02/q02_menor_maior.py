from utils import escrever, obter_numero_real
def main():
    num1 = obter_numero_real("Digite o primeiro número: ")
    num2 = obter_numero_real("Digite o segundo número: ")
    escrever("Entrada inválida. Por favor, digite números.")

    if num1 > num2:
        maior = num1
        menor = num2
    elif num2 > num1:
        maior = num2
        menor = num1
    else:
        escrever("Os números são iguais.")
        return

    escrever(f"O menor número é: {menor}")
    escrever(f"O maior número é: {maior}")

main()