with open("Dane_PR2/sygnaly.txt") as o:
    content = o.readlines()
    topWord = ""
    diffChars = 0
    for word in content:
        tmpCharList = []
        word = word[:-1]
        for char in word:
            if char not in tmpCharList:
                tmpCharList.append(char)
        if len(tmpCharList) > diffChars:
            diffChars = len(tmpCharList)
            topWord = word
    print(topWord, diffChars)
