todo_list = [[] * 0 for i in range(10)]
result = []


def add_to_list(index, task):
    todo_list[index].append(task)

def execute(command):
    splitted = command.split("-")
    index = int(splitted[0])-1
    task = splitted[1]
    add_to_list(index, task)


while True:
    command = input()
    if command == "End":
        for task in todo_list:
            if len(todo_list) > 0:
                for n in task:
                    result.append(n)
        print(result)
        break
    else:
        execute(command)