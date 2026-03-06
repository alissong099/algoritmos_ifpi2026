from utils import escrever, obter_inteiro

def main():
    dia_nasc = obter_inteiro('Digite o dia de nascimento: ')
    mes_nasc = obter_inteiro('Digite o mês de nascimento: ')
    ano_nasc = obter_inteiro('Digite o ano de nascimento: ')
    dia_at = obter_inteiro('Digite o dia atual: ')
    mes_at = obter_inteiro('Digite o mês atual: ')
    ano_at = obter_inteiro('Digite o ano atual: ')

    idade = obter_data_exata(dia_nasc, mes_nasc, ano_nasc, dia_at, mes_at, ano_at)

    escrever(idade)

def obter_data_exata(d_n, m_n, a_n, d_at, m_at, a_at):
    anos = a_at - a_n
    meses = m_n - m_at
    dias = d_n - d_at
    
    if m_at < m_n:
        anos -= 1
        meses = (m_at + 12) - m_n
    if d_at < d_n:
        meses -= 1
        dias = (d_at + 30) - d_n    
    return f'A sua idade exata é {anos} anos, {meses} meses e {dias} dias.'    

main()    