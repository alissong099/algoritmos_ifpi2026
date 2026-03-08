from utils import obter_texto, escrever

def main():
    letra = obter_texto('Informe o seu sexo, (M) ou (F): ')

    verficar = sexo_valido(letra)

    escrever(verficar)

def sexo_valido(l):
    if l == 'M':
        return 'Seu sexo é masculino'
    elif l == 'F':
        return 'Seu sexo é feminino'
    else:
        return 'Sexo inválido'


main()    