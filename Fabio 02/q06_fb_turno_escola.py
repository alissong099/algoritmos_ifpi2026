from utils import escrever, obter_texto

def main():
    turno = obter_texto('Informe o turno que você estuda, matutino(M), vespertino(V) ou nortuno(N): ')

    mensagem = obter_mensagem_turno(turno)

    escrever(mensagem)

def obter_mensagem_turno(t):
    if t == 'M':
        return 'Bom Dia!'
    elif t == 'V':
        return 'Boa Tarde!'
    elif t == 'N':
        return 'Boa Noite'
    else:
        return 'Turno inválido'


main()