minutos = int(input("Digite os minutos: "))

minutos_para_horas = minutos // 60
minutos_restantes = (minutos % 60)

print(f"{minutos} minutos equivalem a {minutos_para_horas} horas e {minutos_restantes} minutos")