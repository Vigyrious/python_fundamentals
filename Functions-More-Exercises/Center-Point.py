import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def find_diagonal(x, y):
    a = int(x) * 1.0
    b = int(y) * 1.0
    return math.sqrt(abs((pow(a, 2)) + (pow(b, 2))))


if find_diagonal(x1, y1) < find_diagonal(x2, y2):
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")

