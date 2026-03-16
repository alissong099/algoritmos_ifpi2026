from utils import escrever, obter_numero_real

def main():
    nota1 = obter_numero_real('Informe a primeira nota: ')
    nota2 = obter_numero_real('Informe a segunda nota: ')

    resultado = verificar_aprovacao(nota1, nota2)

    escrever(resultado)

def verificar_aprovacao(n1, n2):
    media =  (n1 + n2) / 2
    if media >= 9 and media <= 10:
        return f'''
        Notas: {n1} e {n2}
        Média obtida: {media}
        Conceito: A
        APROVADO'''
    elif media >= 7.5:
        return f'''
        Notas: {n1} e {n2}
        Média obtida: {media}
        Conceito: B
        APROVADO'''
    elif media >= 6.0:
        return f'''
        Notas: {n1} e {n2}
        Média obtida: {media}
        Conceito: C
        APROVADO'''
    elif media >= 4.0:
        return f'''
        Notas: {n1} e {n2}
        Média obtida: {media}
        Conceito: D
        REPROVADO'''
    else:
        return f'''
        Notas: {n1} e {n2}
        Média obtida: {media}
        Conceito: E
        REPROVADO'''



main()