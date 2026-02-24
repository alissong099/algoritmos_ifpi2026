numerador1 = int(input("Informe o númerador da primeira fração: "))
denominador1 = int(input("Informe o denominador da primeira fração: "))
numerador2 = int(input("Informe o númerador da segunda fração: "))
denominador2 = int(input("Informe o denominador da segunda fração: "))

soma_numerador = (numerador1 * denominador2) + (denominador1 * numerador2)
soma_denominador = denominador1 * denominador2

print(f"A soma das frações {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a {soma_numerador}/{soma_denominador}")