'''Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%'''
from utils import escrever, obter_numero_real, obter_inteiro

def main():
    valor_hora = obter_numero_real('Informe o valor da sua hora: ')
    horas = obter_inteiro('Informe quantas horas trabalhadas no mês: ')

    folha_pagamento = obter_folha_pagamento(valor_hora, horas)

    escrever(folha_pagamento)

def obter_folha_pagamento(v_h, h):



main()