import re
data = input()
pattern = r'\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}'
result = re.finditer(pattern, data)
new_list = [p.group(0) for p in result]
for date in new_list:
    day, month, year = re.split(r'[\./-]', date)
    print(f"Day: {day}, Month: {month}, Year: {year}")