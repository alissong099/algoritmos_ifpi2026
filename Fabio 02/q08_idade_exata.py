def calcular_idade(dia_n, mes_n, ano_n, dia_a, mes_a, ano_a):
    idade = ano_a - ano_n
    
    if (mes_a < mes_n) or (mes_a == mes_n and dia_a < dia_n):
        idade = idade - 1
        
    return idade

def main():
    print("--- Calculadora de Idade Exata ---")
    dn = int(input("Dia de nascimento: "))
    mn = int(input("Mês de nascimento: "))
    an = int(input("Ano de nascimento: "))
    
    da = int(input("Dia atual: "))
    ma = int(input("Mês atual: "))
    aa = int(input("Ano atual: "))

    total_anos = calcular_idade(dn, mn, an, da, ma, aa)
    print(f"Você tem exatamente {total_anos} anos.")


main()