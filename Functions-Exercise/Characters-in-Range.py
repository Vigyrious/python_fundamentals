char_a = input()
char_b = input()


def solve(a,b):
    for i in range(ord(a)+1, ord(b)):
        print(f"{chr(i)}", end=" ")


solve(char_a, char_b)