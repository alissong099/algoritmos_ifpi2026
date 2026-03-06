from utils import obter_inteiro, escrever

def main():
    h_ini = obter_inteiro("Hora início: ")
    m_ini = obter_inteiro("Minuto início: ")
    h_fim = obter_inteiro("Hora fim: ")
    m_fim = obter_inteiro("Minuto fim: ")
    
    resultado = calcular_duracao(h_ini, m_ini, h_fim, m_fim)
    
    escrever(resultado)


def calcular_duracao(h1, m1, h2, m2):
    inicio_total = h1 * 60 + m1
    fim_total = h2 * 60 + m2

    if fim_total <= inicio_total:
        fim_total += 24 * 60  # Adiciona 24h se terminou no dia seguinte

    duracao_minutos = fim_total - inicio_total
    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60

    return f"Duração: {horas}h e {minutos}min"


main()