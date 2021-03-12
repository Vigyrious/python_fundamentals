from tkinter import *

app = Tk()


def delete_task():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        new_lines = []
    with open("data.txt", "w") as f:
        for i in range(1, len(lines) + 1):
            if i != int(delete_text.get()):
                new_lines.append(lines[i-1])
        f.writelines(i for i in new_lines)
    show_tasks()

def read_tasks():
    tasks_zapis = []
    with open("data.txt", "r") as file:
        tasks_zapis = file.readlines()
    return tasks_zapis


def show_tasks():
    text.delete(1.0, END)
    global counter
    counter = 1
    global task
    for task in read_tasks():
        text.insert("end -1 chars", f"{counter}.{task}")
        counter += 1

def add_task():
    with open("data.txt", "a") as file:
        file.writelines(f"{entry_text.get()}\n")
        entry_text.delete(0, END)
    show_tasks()


def layot_settings():
    app.geometry("400x400")
    app.configure(background='white')


def elements_settings():
    label = Label(app, text="Enter a task:", bg="black", fg="white", font=("Helvetica", 8))
    label.grid(row=0, column=0)
    global entry_text
    entry_text = Entry(app)
    entry_text.grid(row=1, column=0, pady=5, padx=10)
    # all_tasks_box =
    button_submit = Button(app, text="Submit",bg="white", command=add_task)
    button_submit.grid(row=3, column=0)
    global text
    text = Text(app, height=15, width=15)
    text.grid(row=4, column=0, padx=10, pady=5)
    button_show = Button(app, text="Show tasks", bg="white", command=show_tasks)
    button_show.grid(row=5, column=0)
    button_delete = Button(app, text="Delete № task", bg="white", command=delete_task)
    button_delete.grid(row=3, column=1, padx=100,)
    global delete_text
    delete_text = Entry(app)
    delete_text.grid(row=1, column=1, pady=5, padx=10)
    delete_entry_label = Label(app, text="Enter the task № that needs to be deleted", bg="black", fg="white", font=("Helvetica", 8))
    delete_entry_label.grid(row=0, column=1)


layot_settings()
elements_settings()
mainloop()
