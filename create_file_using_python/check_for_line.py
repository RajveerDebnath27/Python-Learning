def check_for_word():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            line = f.readline()
            if word in line:
                print("word:",line_no)
                return
            line_no+=1


    return -1

check_for_word()