numero = int(input("Digite um número inteiro de 3 digitos: "))

centena = numero // 100
resto = numero % 100
dezena = resto // 10 
unidade = numero % 10
somatorio = centena + dezena + unidade
print(f'O somatório dos dígitos do número {numero} é {somatorio}')