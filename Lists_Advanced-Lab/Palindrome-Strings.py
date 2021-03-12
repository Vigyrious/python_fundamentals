words = input().split(" ")
searched = input()
result = []
palindrome_count = 0
for word in words:
    current_word = ""
    for i in range(len(word)-1,-1,-1):
        current_word += word[i]
    if current_word == word:
        result.append(word)
    if current_word == searched:
        palindrome_count += 1
print(result)
print(f"Found palindrome {palindrome_count} times")