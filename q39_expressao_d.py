a = int(input("Digite o valor(A): "))
b = int(input("Digite o valor(B): "))
c = int(input("Digite o valor(C): "))

r = (a + b) ** 2
s = (b + c) ** 2

d = (r + s) / 2

print(f"O resultado da expressão D = R + S / 2 onde R = (A + B)² e S = (B + C)² resulta em D = {r} + {s} / 2 = {d}")