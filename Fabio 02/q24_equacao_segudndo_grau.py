from utils import obter_numero_real, escrever

def main():
    escrever("--- Calculadora de Equação de 2° Grau ---")
    a = obter_numero_real("Digite o coeficiente A: ")
    b = obter_numero_real("Digite o coeficiente B: ")
    c = obter_numero_real("Digite o coeficiente C: ")

    resultado = resolver_segundo_grau(a, b, c)
    
    escrever(resultado)


def resolver_segundo_grau(a, b, c):
    if a == 0:
        return "Erro: O coeficiente 'A' deve ser diferente de 0 para ser uma equação de 2° grau."
    
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        return f"Delta = {delta}. A equação não possui raízes reais."
    elif delta == 0:
        x = (-b) / (2 * a)
        return f"Delta = 0. A equação possui uma raiz real: {x:.2f}"
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        return f"Delta = {delta}. As raízes são: x1 = {x1:.2f} e x2 = {x2:.2f}"



main()