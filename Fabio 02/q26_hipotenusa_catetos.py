from utils import obter_numero_real, escrever

def main():
    escrever("--- Identificador de Lados de Triângulo ---")
    l1 = obter_numero_real("Digite o valor do primeiro lado: ")
    l2 = obter_numero_real("Digite o valor do segundo lado: ")
    l3 = obter_numero_real("Digite o valor do terceiro lado: ")

    resultado = identificar_lados_triangulo(l1, l2, l3)
    
    escrever(resultado)


def identificar_lados_triangulo(a, b, c):
    if a >= b and a >= c:
        hipotenusa = a
        cateto1 = b
        cateto2 = c
    elif b >= a and b >= c:
        hipotenusa = b
        cateto1 = a
        cateto2 = c
    else:
        hipotenusa = c
        cateto1 = a
        cateto2 = b
    
    return f"Hipotenusa: {hipotenusa}\nCatetos: {cateto1} e {cateto2}"


main()