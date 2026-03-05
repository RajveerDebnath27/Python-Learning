name = str(input("Enter any word: "))


def str_reverse(word,idx=len(name)):

    if idx == 0:
        return None

    if idx == 1:
        print(word[idx-1], end="")
    else:
        print(word[idx-1], end=", ")


    return str_reverse(word,idx-1)

str_reverse(name)