count = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
cost = 0
for i in range(1, count+1):
    if i % 12 == 0:
        cost += armor
    if i % 6 == 0:
        cost += shield
    if i % 3 == 0:
        cost += sword
    if i % 2 == 0:
        cost += helmet
print(f"Gladiator expenses: {cost:.2f} aureus")