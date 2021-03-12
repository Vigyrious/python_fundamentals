tickets = input().split(", ")
winners = ['@', '^', '#', '$']
symbol = ""


def checker(ticket):
    winner_left = 0
    winner_right = 0
    global symbol
    left_side = ticket[0:10]
    right_side = ticket[10:20]
    for winner in winners:
        if winner * 6 in left_side and winner * 6 in right_side:
            count_left = left_side.count(winner)
            count_right = right_side.count(winner)
            count = min(count_right,count_left)
            print(f'ticket "{ticket}" - {count}{winner}')
            return True
    return False


def jackpot(ticket):
    global symbol
    for winner in winners: #winner =
        if ticket.count(winner) == 20:
            symbol = winner
            return True
    return False


for t in tickets:
    ticket = t.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    if jackpot(ticket):
        print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
        symbol = ""
        continue
    if checker(ticket):
        continue
    print(f'ticket "{ticket}" - no match')