from utils import escrever, obter_inteiro
def verificar_se_e_primo(n):
    if n <= 1:
        return 'Não é primo'
    
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0:
        return 'Não é primo'   
    elif n > 3 and n % 3 == 0:
        return 'Não é primo'
    elif n > 5 and n % 5 == 0:
        return 'Não é primo'
    elif n > 7 and n % 7 == 0:
        return 'Não é primo'
    elif n > 11 and n % 11 == 0:
        return 'Não é primo'
    else:  
        return 'É primo'

def main():
    escrever("--- Verificador de Primos (Simples) ---")
    numero = obter_inteiro("Digite um número: ")
    
    if verificar_se_e_primo(numero):
        escrever(f"O número {numero} é primo (ou não possui divisores simples).")
    else:
        escrever(f"O número {numero} não é primo.")

main()   