x1_ponto1 = int(input("Informe o (x1) do ponto 1: "))
y1_ponto1 = int(input("Informe o (y1) do ponto 1: "))
x2_ponto2 = int(input("Informe o (x2) do ponto 2: "))
y2_ponto2 = int(input("Informe o (y2) do ponto 2: "))

distancia = ((x2_ponto2 - x1_ponto1)**2 + (y2_ponto2 - y1_ponto1) ** 2) ** 0.5

print(f"A distancia entre os pontos 1 ({x1_ponto1},{y1_ponto1}) e ({x2_ponto2},{y2_ponto2}) é {distancia}")