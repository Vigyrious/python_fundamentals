employees = [int(i) for i in input().split(" ")]
factor = int(input())
new_employees = [int(i) * factor for i in employees]
avg = sum(new_employees) / len(employees)
happy_employees = [int(i) for i in new_employees if i >= avg]

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")