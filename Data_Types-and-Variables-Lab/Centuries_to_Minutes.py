import math
century = int(input())
years = century * 100
days = math.floor(365.2422 * years)
hours = days * 24
minutes = hours * 60
print(f"{century} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
