months = int(input("Please indicate how many months will be converted into years and months: "))

years = months // 12
remaining_months = months % 12

print(f"{months} months are equivalent to {years} years and {remaining_months} months")