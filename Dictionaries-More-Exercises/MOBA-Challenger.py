dect_players = {}
command = input()


def add_player(dect_players, player, position, skill):
    if player not in dect_players:
        dect_players[player] = {}
    if position not in dect_players[player]:
        dect_players[player][position] = 0
    if int(skill) > dect_players[player][position]:
            dect_players[player][position] = int(skill)
    return dect_players

def fight(dect_players, player1, player2):
    if player1 not in dect_players or player2 not in dect_players:
        return dect_players
    is_common = False
    for positions in dect_players[player1]:
        for positions1 in dect_players[player2]:
            if positions == positions1:
                is_common = True
                break
    if is_common:
        player1_score = 0
        player2_score = 0
        for position, score in dect_players[player1].items():
            player1_score += int(score)
        for position, score in dect_players[player2].items():
            player2_score += int(score)
        if player1_score > player2_score:
            dect_players.pop(player2)
        elif player2_score > player1_score:
            dect_players.pop(player1)
    return  dect_players



while command != "Season end":
    data_list = command.split(" -> ")
    if len(data_list) > 2:
        player, position, skill = command.split(" -> ")
        dect_players = add_player(dect_players, player, position, skill)
    else:
        player1, player2 = command.split(" vs ")
        dect_players = fight(dect_players, player1, player2)
    command = input()
sorted_dect = {}
for name in dect_players:
    for position, score in dect_players[name].items():
        if name not in sorted_dect:
            sorted_dect[name] = 0
        sorted_dect[name] += int(score)
for name, points in sorted(sorted_dect.items(), key=lambda x:(-x[1],x[0])):
    print(f"{name}: {points} skill")
    for position, score in sorted(dect_players[name].items(),key=lambda y:(-y[1],y[0])):
        print(f"- {position} <::> {score}")