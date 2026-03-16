from utils import escrever, obter_inteiro, obter_numero_real

def main():
    valor_hora = obter_numero_real('Informe o valor da hora: ')
    horas = obter_inteiro('Informe as horas trabalhadas no mês: ')

    pagamento = obter_folha_pagamento(valor_hora, horas)

    escrever(pagamento)

def obter_folha_pagamento(v_h, h):
    s_bruto = v_h * h
    ir = 0
    inss = 10
    fgts = s_bruto * 0.11
    desconto_inss = s_bruto * inss / 100

    if s_bruto > 2500:
        ir = 20
        desconto_ir = s_bruto * ir / 100
        t_descontos = desconto_ir + desconto_inss
        s_liquido = s_bruto - t_descontos
    elif s_bruto > 1500:
        ir = 10
        desconto_ir = s_bruto * ir / 100
        t_descontos = desconto_ir + desconto_inss
        s_liquido = s_bruto - t_descontos
    elif s_bruto > 900:
        ir = 5
        desconto_ir = s_bruto * ir / 100
        t_descontos = desconto_ir + desconto_inss
        s_liquido = s_bruto - t_descontos
    else:
        ir = 0
        desconto_ir = s_bruto * ir / 100
        t_descontos = desconto_ir + desconto_inss
        s_liquido = s_bruto - t_descontos
    
    return f'''
Salário Bruto: ({v_h}*{h})  : R$ {s_bruto:.2f}
(-) IR ({ir}%)              : R$ {desconto_ir:.2f}
(-) INSS ({inss}%)          : R$ {desconto_inss:.2f}
FGTS (11%)                  : R$ {fgts:.2f}
Total de descontos          : R$ {t_descontos:.2f}
Salário Liquido             : R$ {s_liquido:.2f}'''



main()