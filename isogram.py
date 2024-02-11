def count_word(word):
    word_list = list(word)
    dict_letter = {}
    for i in word_list:
        count = word_list.count(i)
        dict_letter[i] = count
        count = 0
    print(dict_letter)
    return dict_letter

def word_isogram(word):
    flag = True
    dict_letter = count_word(word)
    for i in dict_letter:
        if dict_letter[i] > 1:
            flag = False
    return flag

print("Determine if a word or phrase is an isogram")
word = input("Input a word: ")

flag = word_isogram(word)

if flag == True:
    print(f"Word {word} is isogram")
else:
    print(f"word {word} is not isogram")



