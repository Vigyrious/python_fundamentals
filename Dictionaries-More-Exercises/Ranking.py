dect_contests = {}
dect_submissions = {}
command = input()

while command != "end of contests":
    contest, password = command.split(":")
    dect_contests[contest] = 0
    dect_contests[contest] = password
    command = input()

command = input()

while command != "end of submissions":
    contest, password, username, points = command.split("=>")
    if contest in dect_contests and password == dect_contests[contest]:
        if username not in dect_submissions:
            dect_submissions[username] = {}
        if contest not in dect_submissions[username]:
            dect_submissions[username][contest] = int(points)
        else:
            if int(points) > dect_submissions[username][contest]:
                dect_submissions[username][contest] = int(points)
    command = input()

max_points   = 0
biggest_user = ""
for user in dect_submissions:
    current  = 0
    for subject in dect_submissions[user]:
        current += dect_submissions[user][subject]
    if current > max_points:
        max_points = current
        biggest_user = user
print(f"Best candidate is {biggest_user} with total {max_points} points.")
print("Ranking:")
for user in sorted(dect_submissions):
    print(f"{user}")
    for contest, points in sorted(dect_submissions[user].items(),key=lambda x:-x[1]):
        print(f"#  {contest} -> {points}")