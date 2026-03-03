def verificar_triangulo_angulo(a1, a2, a3):
    if a1 <= 0 or a2 <= 0 or a3 <= 0:
        return "Inválido (ângulo zero ou negativo)"
    
    soma = a1 + a2 + a3
    
    if soma == 180:
        if a1 < 90 and a2 < 90 and a3 < 90:
            return "Acutângulo"
        elif a1 == 90 or a2 == 90 or a3 == 90:
            return "Retângulo"
        else:
            return "Obtusângulo"
    else:
        return "Não forma um triângulo (soma diferente de 180)"

def main():
    print("--- Analisador de Ângulos de Triângulo ---")
    ang1 = float(input("Digite o 1º ângulo: "))
    ang2 = float(input("Digite o 2º ângulo: "))
    ang3 = float(input("Digite o 3º ângulo: "))

    resultado = verificar_triangulo_angulo(ang1, ang2, ang3)
    print(f"Resultado: {resultado}")

main()