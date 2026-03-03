from utils import escrever, obter_inteiro
def main():
    escrever('------ Validador de Datas ------')
    dia = obter_inteiro("Digite o dia: ")
    mes = obter_inteiro("Digite o mês: ")
    ano = obter_inteiro("Digite o ano: ")

    validar = data_valida(dia, mes, ano)

    escrever(validar)

def data_valida(d, m, a):
    if d > 31 and m > 12 and a < 1:
        return 'A data é inválida pois não há data com mais de 31 dias, mais de 12 meses e ano menor que 1'
    elif d > 31:
        return 'A data é inválida pois não há nenhum mês com mais de 31 dias'
    elif m > 12:
        return 'A data é inválida pois não há mais de 12 meses no ano'
    elif a < 1:
        return 'A data é inválida pois não há ano menor que 1'
    elif d == 0:
        return 'A data é inválida pois não há nenhum mês com 0 dias'
    elif m == 0:
        return 'A data é inválida pois não há mais mês 0 no ano'
    else:
        return 'A data é válida.'

main()    