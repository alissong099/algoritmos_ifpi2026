from utils import escrever, obter_numero_real, obter_texto

def main():
    litros = obter_numero_real('Informe quantos litros foram abastecidos: ')
    tipo = obter_texto('Informe o tipo do combustível (A-álcool ou G-gasolina): ')

    a_pagar = calcular_desconto(litros, tipo)

    escrever(a_pagar)

def calcular_desconto(l, t):
    preco_g = 2.50
    preco_a = 1.90
    total = 0

    if l > 20 and t == 'A':
        preco_a = preco_a - preco_a * 0.05
        total = preco_a * l
    else:
        preco_a = preco_a - preco_a * 0.03
        total = preco_a * l
    
    if l > 20 and t == 'G':
        preco_g = preco_g - preco_g * 0.06
        total = preco_g * l
    else:
        preco_g = preco_g - preco_g * 0.04
        total = preco_g * l

    return f'O total a pagar é de R${total:.2f}'




main()