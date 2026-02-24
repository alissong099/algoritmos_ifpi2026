numero = int(input("Digite um número de 4 digitos: "))

milhar = numero // 1000
centena = (numero // 100) % 10
resto = numero % 100
dezena = resto // 10
unidade = numero % 10

soma = milhar + centena + dezena + unidade

print(f"A soma dos elementos: {milhar} + {centena} + {dezena} + {unidade} é igual a {soma}")