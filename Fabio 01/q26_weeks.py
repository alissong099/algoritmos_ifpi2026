days = int(input("Please indicate how many days will be converted into weeks: "))
weeks = days // 7
remaining_days = days % 7

print(f"{days} days are equivalent to {weeks} weeks and {remaining_days} days")