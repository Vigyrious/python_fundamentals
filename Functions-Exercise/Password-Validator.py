# A - 65, Z - 90, a - 97, z - 122, 0 - 48, 9 - 57

password = input()


def password_checker(a):
    isForbidden = False
    isValid = True
    notDigit = 0
    if not 6 <= len(a) <= 10:
        print("Password must be between 6 and 10 characters")
        isValid = False
    for i in range(len(a)):
        current_symbol = ord(a[i])
        if current_symbol in range(65, 91) or current_symbol in range(97, 123) or current_symbol in range(48,58):
            if current_symbol not in range(48, 58):
                notDigit += 1
        else:
            isForbidden = True
            notDigit += 1
    if isForbidden:
        print("Password must consist only of letters and digits")
        isValid = False
    if len(a) - notDigit < 2:
        print("Password must have at least 2 digits")
        isValid = False
    if isValid:
        print("Password is valid")


password_checker(password)