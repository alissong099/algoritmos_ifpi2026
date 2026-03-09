from utils import escrever, obter_numero_real

def main():
    preco1 = obter_numero_real('Digite o preço do produto 1: ')
    preco2 = obter_numero_real('Digite o preço do produto 2: ')
    preco3 = obter_numero_real('Digite o preço do produto 3: ')

    menor_valor = obter_produto_menor_valor(preco1, preco2, preco3)

    escrever(menor_valor)

def obter_produto_menor_valor(p1, p2, p3):
    menor_preco = p1
    if p2 < p1:
        menor_preco = p2
    if p3 < p1:
        menor_preco = p3
    
    return f'O produto com o menor preço é o produto com o preço de {menor_preco}'


main()