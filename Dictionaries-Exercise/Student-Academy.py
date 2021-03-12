rows = int(input())
dect = {}
for i in range(rows):
    name = input()
    grade = float(input())
    if name not in dect:
        dect[name] = []
    dect[name].append(grade)
for student, grades in dect.items():
    dect[student] = (sum(grades) / len(grades))
new_dec = {k:v for k,v in dect.items() if dect[k] >= 4.5}
# for student in sorted(new_dec, key=lambda x:x[1]):
for student, grade in sorted(new_dec.items(), key=lambda x: x[1],reverse=True):
    print(f"{student} -> {grade:.2f}")