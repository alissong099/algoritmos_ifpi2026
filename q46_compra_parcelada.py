valor_item = float(input("Informe o valor do produto: "))

parcelas = valor_item // 3
resto_parcelas = valor_item % 3
entrada = parcelas + resto_parcelas

print(f"A entrada será de {entrada} e as duas parcelas são iguais a {parcelas}")