dect_languages = {}
command = input()
while command != "no more time":
    name, language, points = command.split(" -> ")
    if language not in dect_languages:
        dect_languages[language] = {}
    if name not in dect_languages[language]:
        dect_languages[language][name] = int(points)
    else:
        if int(points) > dect_languages[language][name]:
            dect_languages[language][name] = int(points)
    command = input()
for name in dect_languages:
    count = 1
    print(f"{name}: {len(dect_languages[name])} participants")
    for name, points in sorted(dect_languages[name].items(), key= lambda x:(-x[1], x[0])):
        print(f"{count}. {name} <::> {points}")
        count += 1
print("Individual standings:")
dect_score = {}
for language in dect_languages:
    for name, score in dect_languages[language].items():
        if name not in dect_score:
            dect_score[name] = 0
            dect_score[name] = int(score)
        else:
            dect_score[name] += int(score)
count = 1
for name, points in sorted(dect_score.items(), key= lambda x:(-x[1],x[0])):
    print(f"{count}. {name} -> {points}")
    count += 1
