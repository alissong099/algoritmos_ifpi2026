numero = int(input("Digite um número de 3 digitos "))

centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = numero % 10

inverso = (unidade * 100) + (dezena * 10) + centena

diferenca = numero - inverso

print(f"A diferença entre os números {numero} e {inverso} é de {diferenca}")