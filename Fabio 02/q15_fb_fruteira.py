from utils import obter_inteiro, escrever

def main():
    qtd_macas = obter_inteiro('Informe quantos quilos de maçãs você vai levar: ')
    qtd_morango = obter_inteiro('Informe quantos quilos de morangos você vai levar: ')

    a_pagar = calcular_desconto(qtd_macas, qtd_morango)

    escrever(a_pagar)

def calcular_desconto(k_mc, k_mr):
    total_k = k_mc + k_mr
    preco_maca = 1.80
    preco_morango = 2.50
    total_a_pagar = 0
    if k_mc > 5:
        preco_maca = 1.50
    
    if k_mr > 5:
        preco_morango = 2.20

    total_a_pagar = preco_morango * k_mr + preco_maca * k_mc

    if total_k > 8 or total_a_pagar > 25:
        total_a_pagar = total_a_pagar - total_a_pagar * 0.10

    return f'O total a pagar é R${total_a_pagar:.2f}'



main()