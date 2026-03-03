def ordenar_crescente(n1, n2, n3):
    if n1 > n2:
        n1, n2 = n2, n1
        
    if n1 > n3:
        n1, n3 = n3, n1
        
    if n2 > n3:
        n2, n3 = n3, n2
        
    return n1, n2, n3

def main():
    print("--- Ordenação de Números ---")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    menor, meio, maior = ordenar_crescente(num1, num2, num3)

    print(f"Os números em ordem crescente são: {menor}, {meio}, {maior}")

main()