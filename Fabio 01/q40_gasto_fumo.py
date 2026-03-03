anos_fumando = int(input("A quantos anos você fuma? "))
cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
preco_carteira = float(input("Qual o preço da carteira de cigarro que você compra? "))

cigarros_totais = (anos_fumando * 365) * cigarros_dia
carteiras_totais = cigarros_totais / 20
gasto_cigarros = carteiras_totais * preco_carteira

print(f"Ao todo você fumou {cigarros_totais} cigarros e gastou {gasto_cigarros:.2f}R$ em cigarros na sua vida.")