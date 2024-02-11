print("Determine if a word or phrase is an isogram")
word = input("Input a word: ")

word_list = list(word)
dict_letter = {}
flag = True

for i in word_list:
    count = word_list.count(i)
    dict_letter[i] = count    
    count = 0

for i in dict_letter:
    if dict_letter[i] > 1:
        flag = False


if flag == True:
    print(f"Word {word} is isogram")
else:
    print(f"word {word} is not isogram")

print(dict_letter)


