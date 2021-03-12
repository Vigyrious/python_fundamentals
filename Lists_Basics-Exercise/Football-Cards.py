teamA = 11
teamB = 11
string = input()
new_List = string.split(" ")
teamA_list = []
teamB_list = []
isTerminated = False
for i in range (1,12):
    teamA_list.append("A-"+str(i))
    teamB_list.append("B-"+str(i))
for card in new_List:
    if card in teamA_list:
        teamA_list.remove(card)
    elif card in teamB_list:
        teamB_list.remove(card)
    if len(teamA_list) < 7 or len(teamB_list) < 7:
        isTerminated = True
        break
print(f"Team A - {len(teamA_list)}; Team B - {len(teamB_list)}")
if isTerminated:
    print("Game was terminated")
