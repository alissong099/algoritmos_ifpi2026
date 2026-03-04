def escrever(conteudo: str):
  print(conteudo)


def obter_texto(instrucoes = 'Digite algo: '):
  entrada = input(instrucoes)
  return entrada


def obter_inteiro(instrucoes = 'Digite um inteiro: '):
  numero = int(input(instrucoes))
  return numero


def obter_numero_real(instrucoes = 'Digite um real: '):
  numero = float(input(instrucoes))
  return numero

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

def eh_impar_ou_par(n):
    if n % 2 == 0:
        return 'O número é par'
    else:
        return 'O número é ímpar'
