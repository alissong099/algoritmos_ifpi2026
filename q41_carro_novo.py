custo_fabrica = float(input("Informe o valor de fábrica do carro: "))

impostos = custo_fabrica * 0.45
distribuidor = custo_fabrica * 0.28
custo_total = custo_fabrica + impostos + distribuidor

print(f"O valor do imposto é de {impostos:.2f}R$ e a percentagem do distribuidor de 28% resulta em {distribuidor:.2f}R$, totalizando {custo_total}R$ gastos no carro novo. ")