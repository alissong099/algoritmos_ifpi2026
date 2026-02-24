numero = int(input("Digite um número de três digitos: "))

centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = numero % 10

print(f"O inverso do número {numero} é {unidade}{dezena}{centena}")