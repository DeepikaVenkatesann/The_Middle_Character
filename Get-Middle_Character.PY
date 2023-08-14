def getmiddlecharacters(word):
    length = len(word)
    middleindex = length // 2

    if length % 2 == 1:
        return word[middleindex]
    else:
        return word[middleindex - 1: middleindex + 1]

word = "CHALLENGE"
middlechars = getmiddlecharacters(word)
print(middlechars)
