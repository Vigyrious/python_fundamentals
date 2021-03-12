import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())



def closest(a, b, c, d):

    first = math.sqrt(pow(abs(a), 2) + pow(abs(b), 2))
    second = math.sqrt(pow(abs(c), 2) + pow(abs(d), 2))
    if first > second:
        print(f"({int(c)}, {int(d)})({int(a)}, {int(b)})")
    else:
        print(f"({int(a)}, {int(b)})({int(c)}, {int(d)})")


def longest(a, b, c, d, e, f, g, h):
    first = math.sqrt(pow(abs(a-c), 2) + pow(abs(b-d), 2))
    second = math.sqrt(pow(abs(e-g), 2) + pow(abs(f-h), 2))
    if first >= second:
        closest(a, b, c, d)
    else:
        closest(e, f, g, h)


longest(x1, y1, x2, y2, x3, y3, x4, y4)

