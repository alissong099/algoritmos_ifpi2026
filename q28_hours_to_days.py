hours = int(input("PLease indicate how many hours will be converted into weeks, days and hours: "))

days = hours // 24
weeks = days // 7
remaining_hours = hours % 24

print(f"{hours} hours are equivalent to {weeks} weeks, {days} days and {remaining_hours} hours")