number = int(input("Enter the 4-digit binary number to convert to decimal: "))

thousand = number // 1000
hundred = (number // 100) % 10
rest = number % 100
dozen = rest // 10
unit = number % 10

binary1 = unit * 1
binary2 = dozen * 2
binary3 = hundred * 4
binary4 = thousand * 8

decimal = binary1 + binary2 + binary3 + binary4

print(f"{number} binary number converted to decimal >> {decimal}")