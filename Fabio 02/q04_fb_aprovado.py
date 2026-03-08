from utils import obter_numero_real, escrever

def main():
    nota1 = obter_numero_real('Digite a primeira nota: ')
    nota2 = obter_numero_real('Digite a segunda nota: ')

    verificar = resultado_aluno(nota1, nota2)

    escrever(verificar)

def resultado_aluno(n1, n2):
    media = (n1 + n2) / 2
    
    if media == 10:
        return 'Aprovado com Distinção'
    elif media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'


main()