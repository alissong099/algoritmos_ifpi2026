nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso1 = int(input("Digite o peso da primeira nota: "))
peso2 = int(input("Digite o peso da segunda nota: "))
peso3 = int(input("Digite o peso da terceira nota: "))


media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A media ponderada do aluno é de {media_ponderada}")