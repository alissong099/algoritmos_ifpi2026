metros = int(input("Digite quantos metros serão percorridos hoje: "))

quilometros = metros // 1000
resto = metros % 1000

print(f"Você irá percorrer {quilometros} quilometros e {resto} metros")