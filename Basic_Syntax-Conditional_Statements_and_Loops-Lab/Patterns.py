num = int(input())
code = ""
for i in range(num+1):
    for j in range(i):
        code += "*"
    print(code)
    code = ""
for i in range(num-1, 0, -1):
    for j in range(i):
        code += "*"
    print(code)
    code = ""