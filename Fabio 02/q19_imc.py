from utils import obter_numero_real, escrever
def main():
    altura = obter_numero_real('Informe sua altura em m: ')
    peso = obter_numero_real('Informe seu peso em kg: ')

    imc = obter_imc(altura, peso)

    escrever(imc)

def obter_imc(a, p):
    imc = p / a ** 2
    if imc > 30:
        return f'Você está com obesidade mórbida, IMC de {imc:.0f}'
    elif imc >= 25:
        return f'Você está obeso, IMC de {imc:.0f}'
    else:
        return f'Você está com o peso normal, IMC de {imc:.0f}'


main()