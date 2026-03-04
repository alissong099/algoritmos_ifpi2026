from utils import obter_inteiro, escrever
def main():
    num1 = obter_inteiro('Digite o primeiro número: ')
    num2 = obter_inteiro('Digite o segundo número: ')
    num3 = obter_inteiro('Digite o terceiro número: ')
    num4 = obter_inteiro('Digite o quarto número: ')
    num5 = obter_inteiro('Digite o quinto número: ')

    maior_q_media = verificar_maior_q_media(num1, num2, num3, num4, num5)

    escrever(maior_q_media)

def verificar_maior_q_media(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    
    maior_q_media = ''
    if n1 > media:
        maior_q_media = maior_q_media + str(n1) + ' '
    if n2 > media:
        maior_q_media = maior_q_media + str(n2) + ' '
    if n3 > media:
        maior_q_media = maior_q_media + str(n3) + ' '
    if n4 > media:
        maior_q_media = maior_q_media + str(n4) + ' '
    if n5 > media:
        maior_q_media = maior_q_media + str(n5)                    
    return f'A média dos números é {media} e os números maiores que a média são: {maior_q_media}'                                 
        

main()