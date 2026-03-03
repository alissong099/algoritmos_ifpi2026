minutes = int(input("PLease indicate how many minutes will be converted into days, hours and minutes: "))

hours = minutes // 60
days = hours // 24
weeks = days // 7
remaining_minutes = minutes % 60

print(f"{minutes} minutes are equivalent to {weeks} weeks, {days} days, {hours} hours and {minutes} minutes")