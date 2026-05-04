def main():

    votos_candidato_1 = 0
    votos_candidato_2 = 0
    votos_candidato_3 = 0
    votos_candidato_4 = 0
    votos_nulos = 0
    votos_brancos = 0
    votos_validos = 0
    
    opcao = menu_eleicao()
    
    while opcao != 3:
        if opcao == 1:
            votar = menu_voto()
            if votar == 0:
                votos_brancos += 1
            elif votar == 1:
                votos_candidato_1 += 1
                votos_validos += 1
            elif votar == 2:
                votos_candidato_2 += 1
                votos_validos += 1
            elif votar == 3:
                votos_candidato_3 += 1
                votos_validos += 1
            elif votar == 4:
                votos_candidato_4 += 1
                votos_validos += 1
            elif votar == 5:
                votos_nulos += 1
        opcao = menu_eleicao()
        
        if opcao == 2:
            reultado = exibir_resultado(votos_candidato_1, votos_candidato_2, votos_candidato_3, votos_candidato_4, votos_brancos, votos_nulos, votos_validos)
            print(reultado)
    

def menu_eleicao():
    menu_eleicao = '''ELEIÇÕES 2026
    BEM VINDO A URNA ELETRÔNICA
    A SEGUIR AS OPÇÕES
    (1) VOTAR
    (2) VER RESULTADO
    (3) ENCERRAR
    SELECIONE UMA DAS OPÇÕES: '''
    try:
        opcao = int(input(menu_eleicao))
        if opcao != 1 and opcao != 2 and opcao != 3:
            print('Opção inválida!')
        return opcao
    except ValueError:
        print('Escolha inválida! Por favor escolha uma das opções disponivéis.')
        return menu_eleicao()

def menu_voto():
    candidatos = '''CANDIDATOS 2026:
    (0) Voto Branco
    (1) Rogério Silva
    (2) Ricardo Ramos
    (3) Ely Miranda
    (4) Aline Leal
    (5) Voto Nulo
    ESCOLHA UMA DAS OPÇÕES: '''
    try:
        opcao_voto = int(input(candidatos))
        if opcao_voto != 0 and opcao_voto != 1 and opcao_voto != 2 and opcao_voto != 3 and opcao_voto != 4 and opcao_voto != 5:
            print('Opção inválida!')
        return opcao_voto
    except ValueError:
        print('Escolha inválida! Por favor escolha uma das opções disponivéis.')
        return menu_voto()
        
def exibir_resultado(vt1, vt2, vt3, vt4, vt5, vt0, vt_validos):
    percentual_canditado_1 = vt1 / vt_validos * 100
    percentual_canditado_2 = vt2 / vt_validos * 100
    percentual_canditado_3 = vt3 / vt_validos * 100
    percentual_canditado_4 = vt4 / vt_validos * 100
    
    maior_percentual = 0
    vencedor = ''
    
    if percentual_canditado_1 > maior_percentual:
        maior_percentual = percentual_canditado_1
        vencedor = 'Rogério Silva'
    if percentual_canditado_2 > maior_percentual:
        maior_percentual = percentual_canditado_2
        vencedor = 'Ricardo Ramos'
    if percentual_canditado_3 > maior_percentual:
        maior_percentual = percentual_canditado_3
        vencedor = 'Ely Miranda'
    if percentual_canditado_4 > maior_percentual:
        maior_percentual = percentual_canditado_4
        vencedor = 'Aline Leal'
    
    if percentual_canditado_1 == percentual_canditado_2 > maior_percentual:
        vencedor = 'Rogério Silva e Ricardo Ramos'
    elif percentual_canditado_1 == percentual_canditado_3 > maior_percentual:
        vencedor = 'Rogério Silva e Ely Miranda'
    elif percentual_canditado_1 == percentual_canditado_4 > maior_percentual:
        vencedor = 'Rogério Silva e Aline Leal'
    elif percentual_canditado_2 == percentual_canditado_3 > maior_percentual:
        vencedor = 'Ricardo Ramos e Ely Miranda'
    elif percentual_canditado_2 == percentual_canditado_4 > maior_percentual:
        vencedor = 'Ricardo Ramos e Aline Leal'
    elif percentual_canditado_3 == percentual_canditado_4 > maior_percentual:
        vencedor = 'Ely Miranda e Aline Leal'
    
    if maior_percentual < 50:
        return 'Será necessário um segundo turno!'
    else:
        return f'''RESULTADO ELEIÇÃO 2026:
            VOTOS VÁLIDOS: {vt_validos}
            VOTOS BRANCOS: {vt0}
            VOTOS NULOS: {vt5}
        
            PERCENTUAL CANDIDATOS:
            Rogério Silva: {percentual_canditado_1}
            Ricardo Ramos: {percentual_canditado_2}
            Ely Miranda: {percentual_canditado_3}
            Aline Leal: {percentual_canditado_4}
        
            VENCEDOR ELEIÇÕES 2026:
            {vencedor}'''


main()