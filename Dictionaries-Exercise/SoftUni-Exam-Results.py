dect_language = {}
dect_submissions = {}
command = input()


def insert_submissions(dect_submissions, name, points):

    if name not in dect_submissions:
        dect_submissions[name] = int(points)
    if int(dect_submissions[name]) < int(points):
        dect_submissions[name] = int(points)
    return dect_submissions


def insert_language(dect_language, language):
    if language not in dect_language:
        dect_language[language] = 0
    dect_language[language] += 1
    return dect_language


while command != "exam finished":
    data_list = command.split("-")
    if len(data_list) > 2:
        name, language, points = command.split("-")
        dect_submissions = insert_submissions(dect_submissions, name, points)
        dect_language = insert_language(dect_language, language)
    else:
        name = data_list[0]
        dect_submissions.pop(name)
    command = input()
print("Results:")
sorted_submission = sorted(dect_submissions.items(), key=lambda x: (-x[1], x[0]))
sorted_language = sorted(dect_language.items(), key=lambda y: (-y[1], y[0]))
a=5

for name, points in sorted_submission:
    print(f"{name} | {points}")
print("Submissions:")
for languange, count in sorted_language:
    print(f"{languange} - {count}")