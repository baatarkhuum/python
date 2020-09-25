def minion_game(string):
    vowels="AEUIO"
    stuart=0
    kevin=0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin+=len(string)-i
        else:
            stuart+=len(string)-i

    if stuart>kevin:
        print("Stuart "+str(stuart))
    elif kevin>stuart:
        print("Kevin "+ str(kevin))
    else:
        print("Draw")
minion_game('BANANA')
