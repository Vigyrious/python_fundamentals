def grade(num):
    if 2 <= num <= 2.99:
        return "Fail"
    elif 3 <= num <= 3.49:
        return "Poor"
    elif 3.5 <= num <= 4.49:
        return "Good"
    elif 4.5 <= num <= 5.49:
        return "Very Good"
    elif 5.5 <= num <= 6:
        return "Excellent"
intNum = float(input())
print(grade(intNum))