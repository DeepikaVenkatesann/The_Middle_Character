word="challenge"
length_of_word=len(word)
print(length_of_word)

middle_character=word[4:-4]
middle_two_character=word[4:-3]
if(length_of_word%2):
    print("The given word is odd",middle_character)
else:
    print("if the given word is even",middle_two_character)