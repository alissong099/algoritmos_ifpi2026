def main():
    lado_a = float(input("Digite o comprimento do primeiro lado: "))
    lado_b = float(input("Digite o comprimento do segundo lado: "))
    lado_c = float(input("Digite o comprimento do terceiro lado: "))
    print("Entrada inválida. Por favor, digite números.")

    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        print("Não é possível formar um triângulo. O comprimento do lado deve ser maior que 0.")

    condicao1 = lado_a + lado_b > lado_c
    condicao2 = lado_a + lado_c > lado_b
    condicao3 = lado_b + lado_c > lado_a

    if condicao1 and condicao2 and condicao3:
        print("Os números FORMAM um triângulo.")
        
        if lado_a == lado_b and lado_b == lado_c:
            print("Classificação: Triângulo Equilátero (3 lados iguais).")
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print("Classificação: Triângulo Isósceles (2 lados iguais).")
        else:
            print("Classificação: Triângulo Escaleno (3 lados diferentes).")
    else:
        print("Os números NÃO FORMAM um triângulo (a soma de dois lados não é maior que o terceiro lado).")

main()