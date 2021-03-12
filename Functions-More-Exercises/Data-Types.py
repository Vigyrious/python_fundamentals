# •	If the data type is int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.
# •	If the data type is string, surround the input with "$".


type = input()
variable = input()


def is_int(variable):
    return variable * 2


def is_real(variable):
    return "{:.2f}".format(variable * 1.5)


def is_string(string):
    return f"${string}$"


def execute(type, variable):

    if type == "int":
        print(is_int(int(variable)))
    elif type == "real":
        print(is_real(float(variable)))
    elif type == "string":
        print(is_string(variable))


execute(type, variable)