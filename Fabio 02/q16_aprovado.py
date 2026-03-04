from utils import obter_inteiro, escrever
def main():
    nota1 = obter_inteiro('Informe a primeira nota: ')
    nota2 = obter_inteiro('Informe a segunda nota: ')

    media = (nota1 + nota2) / 2

    foi_aprovado = verificar_aprovado(media)
    if foi_aprovado:
        escrever('O aluno foi aprovado')
    elif foi_aprovado == False:
        escrever('O aluno vai realizar o exame final')
        exame = obter_inteiro('Digite a nota obtida no exame: ')
        media_final = media + exame / 2
        foi_aprovado = verificar_aprovado(media_final)

    if foi_aprovado:
        escrever('O aluno foi aprovado após o exame final')   
    else: 
        escrever('O aluno foi reprovado pois sua média foi inferior a 5')
    

def verificar_aprovado(m):
    if m >= 7:
        return True
    elif m >= 5:
        return False

main()    