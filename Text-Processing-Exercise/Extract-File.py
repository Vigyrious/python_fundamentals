string = input().split("\\")
file_extension = string[len(string)-1]
name, ext = file_extension.split(".")
print(f"File name: {name}")
print(f"File extension: {ext}")