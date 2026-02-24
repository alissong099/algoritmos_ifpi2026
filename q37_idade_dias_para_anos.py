dias = int(input("Informe sua idade em dias: "))

anos = dias // 365
resto_anos = dias % 365
meses = resto_anos // 30
dias_restantes = resto_anos % 30

print(f"Sua idade exata é {anos} anos, {meses} meses e {dias_restantes} dias")