from utils import obter_inteiro, escrever

def main():
    escrever("--- Comparador de Datas ---")
    escrever("Data 1:")
    d1, m1, a1 = obter_inteiro("Dia: "), obter_inteiro("Mês: "), obter_inteiro("Ano: ")
    escrever("Data 2:")
    d2, m2, a2 = obter_inteiro("Dia: "), obter_inteiro("Mês: "), obter_inteiro("Ano: ")
    
    resultado = descobrir_data_recente(d1, m1, a1, d2, m2, a2)
    
    escrever(resultado)


def descobrir_data_recente(d1, m1, a1, d2, m2, a2):
    if a1 > a2:
        recente = f"{d1}/{m1}/{a1}"
    elif a2 > a1:
        recente = f"{d2}/{m2}/{a2}"
    else:
        if m1 > m2:
            recente = f"{d1}/{m1}/{a1}"
        elif m2 > m1:
            recente = f"{d2}/{m2}/{a2}"
        else:
            if d1 > d2:
                recente = f"{d1}/{m1}/{a1}"
            elif d2 > d1:
                recente = f"{d2}/{m2}/{a2}"
            else:
                return "As datas são idênticas."
    
    return f"A data mais recente é: {recente}"


main()