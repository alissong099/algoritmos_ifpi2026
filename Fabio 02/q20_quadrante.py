from utils import escrever, obter_inteiro
def main():
    angulo = obter_inteiro('Digite um ângulo de 0  a 360: ')

    quadrante = verificar_quadrante(angulo)

    escrever(quadrante)

def verificar_quadrante(a):
    if a <= 360 and a >= 270:
        return 'O ângulo está no quarto quadrante'
    elif a >= 180:
        return 'O ângulo está no terceiro quadrante'
    elif a >= 90:
        return 'O ângulo está no segundo quadrante'
    else:
        return 'O ângulo está no primeiro quadrante'

main()