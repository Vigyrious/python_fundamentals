num1 = int(input())
num2 = int(input())
num3 = int(input())


def add_and_sub(a, b, c):
    def sumirane(a,b):
        resultat = a + b
        return resultat

    def substract(c):
        resultat1 = sumirane(a,b) - c
        return resultat1
    print(substract(c))




add_and_sub(num1,num2,num3)



