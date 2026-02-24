valor_a = int(input("Informe o valor de (a): "))
valor_b = int(input("Informe o valor de (b): "))
valor_c = int(input("Informe o valor de (c): "))
valor_d = int(input("Informe o valor de (d): "))
valor_e = int(input("Informe o valor de (e): "))
valor_f = int(input("Informe o valor de (f): "))

x = ((valor_c * valor_e) - (valor_b * valor_f)) / ((valor_a * valor_e) - (valor_b * valor_d))
y = ((valor_a * valor_f) - (valor_c * valor_d)) / ((valor_a * valor_e) - (valor_b * valor_d))

print(f"O valor de x é {x} e o valor de y é {y}")

print(f"Portanto a expressão fica dessa forma: C = {valor_a}x{x} + {valor_b}x{y} e F = {valor_d}x{x} + {valor_e}x{y}")