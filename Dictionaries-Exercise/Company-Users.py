command = input()
dect = {}
while command != "End":
    company, id = command.split(" -> ")
    if company not in dect:
        dect[company] = []
    if id not in dect[company]:
        dect[company].append(id)
    command = input()
for companies in sorted(dect):
    print(companies)
    for ids in dect[companies]:
        print(f"-- {ids}")
