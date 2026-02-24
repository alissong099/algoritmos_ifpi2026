anos = int(input("Digite quantos anos você tem: "))
meses = int(input("meses: "))
dias = int(input("e dias: "))

idade_dias = (anos * 365) + (meses * 30) + dias

print(f"A conversão da sua idade para apenas dias resulta em {idade_dias} dias vividos")