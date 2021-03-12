positions = {chr(ele+97): ele+1 for ele in range(26)}
string = input().split()
final = 0
result = 0
for word in string:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])
    if first_letter.isupper():
        number /= positions[first_letter.lower()]
    else:
        number *= positions[first_letter]
    if last_letter.isupper():
        number -= positions[last_letter.lower()]
    else:
        number += positions[last_letter]
    final += number
print(f"{final:.2f}")