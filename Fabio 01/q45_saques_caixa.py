
valor_saque = int(input("Informe o valor do saque: "))

notas_50 = valor_saque // 50
resto_50 = valor_saque % 50
notas_10 = resto_50 // 10
resto_10 = resto_50 % 10
notas_5 = resto_10 // 5
resto_5 = resto_10 % 5
notas_1 = resto_5 // 1

print(f"Para a quantia solicitada {valor_saque} serão {notas_50} notas de R$ 50, {notas_10} notas de R$ 10, {notas_5} notas de R$ 5 e {notas_1} notas de R$ 1")