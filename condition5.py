word = input("Enter a word: ")
reversed=""
for char in word:
    reversed=char+reversed
print(reversed)