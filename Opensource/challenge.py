#copyright : 노관태 - 도전과제 판정


def challenge_1_5_8_9 (chal, num, gold, tower) :
    if chal[0] == 0 :
        if num >= 100 :
            chal[0] = 1
    elif chal[1] == 0 :
        if num >= 200 :
            chal[1] = 1
    elif chal[2] == 0 :
        if num >= 300 :
            chal[2] = 1
    elif chal[3] == 0 :
        if num >= 400 :
            chal[3] = 1
    elif chal[4] == 0:
        if num >= 500:
            chal[4] = 1

    if chal[5] == 0 :
        if gold >= 2000:
            chal[5] = 1
    if chal[6] == 0 :
        if tower[0] and tower[1]:
            if tower[2] and tower[3] :
                chal[6] = 1

    return chal




def challenge_6 (chal, life) :
    if chal[7] == 0:
        if life == 1 :
            chal[7] = 1

    return chal

def challenge_7 (chal, life) :
    if chal[8] == 0:
        if life == 20 :
            chal[8] = 1

    return chal