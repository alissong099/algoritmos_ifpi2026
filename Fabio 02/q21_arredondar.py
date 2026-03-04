from utils import obter_numero_real, escrever
def main():
    numero = obter_numero_real('Digite um número real: ')

    arredondar = arredondamento(numero)

    escrever(arredondar)

def arredondamento(n):
    fracionaria = n - int(n)
    if fracionaria >= 0.5:
        return f'Número arredondado para {int(n)+1}'
    else:
        return f'Número arredondado para {int(n)}'

main()    