def get_character_distance(char1, char2):
    return abs(ord(char2) - ord(char1))


def check_word(checked_word):
    for i in range(len(checked_word) - 1):
        for j in range(i + 1, len(checked_word)):
            if get_character_distance(checked_word[i], checked_word[j]) > 10:
                return True


with open("Dane_PR2/sygnaly.txt") as o:
    content = o.readlines()
    for word in content:
        word = word[:-1]
        if not check_word(word):
            print(word)
