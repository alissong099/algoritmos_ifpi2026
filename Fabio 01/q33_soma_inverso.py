numero  = int(input("Digite um número de 3 digitos para somar o mesmo com seu inverso: "))

centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = numero % 10

inverso = (unidade * 100) + (dezena * 10) + centena

soma = numero + inverso

print(f"A soma dos números {numero} e {inverso} resulta em {soma}")