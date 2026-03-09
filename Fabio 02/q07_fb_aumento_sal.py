from utils import escrever, obter_numero_real

def main():
    salario = obter_numero_real('Informe seu salário para aumento: ')

    novo_salario = calcular_aumento(salario)

    escrever(novo_salario)

def calcular_aumento(s):
    aumento = 0
    novo_s = 0
    percentual = 0
    s_antigo = s
    if s > 1500:
        percentual = 5
        aumento = s * 0.05
        novo_s = s + aumento
    elif s > 700:
        percentual = 10
        aumento = s * 0.10
        novo_s = s + aumento
    elif s > 280:
        percentual = 15
        aumento = s * 0.15
        novo_s = s + aumento
    else:
        percentual = 20
        aumento = s * 0.20
        novo_s = s + aumento
    
    return f'Seu sálario antigo era de R${s_antigo}, recebeu um aumento de {percentual}%, tendo um aumento de R${aumento:.2f}, portanto seu novo salário é de {novo_s:.2f}'



main()