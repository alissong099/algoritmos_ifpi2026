from utils import escrever, obter_inteiro

def main():
    numero = obter_inteiro('Digite um número menor que 1000: ')

    termos = obter_termos_numero(numero)

    escrever(termos)

def obter_termos_numero(n):
    centenas = n // 100
    dezenas = (n % 100) // 10
    unidades = n % 10

    if centenas > 1 and dezenas > 1 and unidades > 1:
        return f'{n} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades'
    elif centenas > 1 and dezenas > 1:
        return f'{n} = {centenas} centenas, {dezenas} dezenas e {unidades} unidade'
    elif centenas > 1 and unidades > 1:
        return f'{n} = {centenas} centenas, {dezenas} dezena e {unidades} unidades'
    elif dezenas > 1 and unidades > 1:
        return f'{n} = {centenas} centena, {dezenas} dezenas e {unidades} unidades'
    if centenas > 1 and dezenas > 1 and unidades == 0:
        return f'{n} = {centenas} centenas e {dezenas} dezenas'
    elif centenas > 1 and dezenas == 0 and unidades > 1:
        return f'{n} = {centenas} centenas, {dezenas} dezenas'
    elif centenas > 1 and unidades > 1:
        return f'{n} = {centenas} centenas, {dezenas} dezena'
    elif dezenas > 1 and unidades > 1:
        return f'{n} = {centenas} centena, {dezenas} dezenas'



main()