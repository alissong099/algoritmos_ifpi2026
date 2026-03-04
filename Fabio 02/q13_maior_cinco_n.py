from utils import obter_inteiro, escrever
def main():
    num1 = obter_inteiro('Digite o primeiro número: ')
    num2 = obter_inteiro('Digite o segundo número diferente do anterior: ')
    num3 = obter_inteiro('Digite o terceiro número diferente do anterior: ')
    num4 = obter_inteiro('Digite o quarto número diferente do anterior: ')
    num5 = obter_inteiro('Digite o quinto número diferente do anterior: ')

    maior = 0
    menor = 0
    maior_menor = verificar_maior_menor(maior, menor, num1, num2, num3, num4, num5)

    escrever(maior_menor)

def verificar_maior_menor(maior, menor, n1, n2, n3, n4, n5):
    maior = n1
    menor = n1
    if n2 > maior:
        maior = n2
    if n2 < menor:
        menor = n2
    if n3 > maior:
        maior = n3
    if n3 < menor:
        menor = n3
    if n4 > maior:
        maior = n4
    if n4 < menor:
        menor = n4
    if n5 > maior:
        maior = n5
    if n5 < menor:
        menor = n5                      
    return f'O maior número é {maior} e o menor é {menor}'                                 
        

main()