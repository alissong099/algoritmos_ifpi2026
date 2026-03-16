from utils import escrever, obter_texto

def main():
    escrever('BEM VINDO A INVESTIGAÇÃO SOBRE UM ASSASSINATO RECENTE')
    escrever('Responda as perguntas somente com SIM ou NÃO.')
    escrever('Vamos iniciar a investigação:')
    pergunta1 = obter_texto('Você telefonou para vítima? ')
    pergunta2 = obter_texto('Esteve no local do crime? ')
    pergunta3 = obter_texto('Mora perto da vítima? ')
    pergunta4 = obter_texto('Devia algo para a vítima? ')
    pergunta5 = obter_texto('Já trabalhou com a vítima? ')
    escrever('Obrigado pelas informações, agora iremos analisar as informações para termos um veredito.')

    veredito = obter_veredito_investigado(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)

    escrever(veredito)

def obter_veredito_investigado(p1, p2, p3, p4, p5):
    respostas_suspeitas = 0
    if p1 == 'SIM':
        respostas_suspeitas += 1
    if p2 == 'SIM':
        respostas_suspeitas += 1
    if p3 == 'SIM':
        respostas_suspeitas += 1
    if p4 == 'SIM':
        respostas_suspeitas += 1
    if p5 == 'SIM':
        respostas_suspeitas += 1  
    
    if respostas_suspeitas == 5:
        return 'Você é o assassino da vítima, será preso agora'
    elif respostas_suspeitas >= 3:
        return 'Você é cúmplice do assassinato'
    elif respostas_suspeitas == 2:
        return 'Você é uma pessoa suspeita, iremos interroga-la novamente em breve'
    else:
        return 'Você é inocente, obrigado pelas informações'




main()