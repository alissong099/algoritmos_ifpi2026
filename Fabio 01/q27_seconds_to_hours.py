seconds = int(input("PLease indicate how many seconds will be converted into hours: "))

hours = seconds // 3600
minutes  = hours * 60
remaining_seconds = seconds % 60

print(f"{seconds} seconds are equivalent to {hours} hours and {minutes} minutes and {remaining_seconds} seconds")