from utils import escrever, obter_numero_real
def main():
    try:
        num1 = obter_numero_real("Digite o primeiro número: ")
        num2 = obter_numero_real("Digite o segundo número: ")
        num3 = obter_numero_real("Digite o terceiro número: ")
    except ValueError:
        escrever("Entrada inválida. Por favor, digite números.")
        return

    maior = num1

    if num2 > maior:
        maior = num2
    
    if num3 > maior:
        maior = num3
        
    escrever(f"O maior número lido é: {maior}")


main()