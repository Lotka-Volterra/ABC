def toNBase(integer, base):
    answerString = ""
    # integerが0より大きい間
    while integer:
        answerString = str(integer % n) + answerString
        integer //= base
    return answerString


n = int(input())
