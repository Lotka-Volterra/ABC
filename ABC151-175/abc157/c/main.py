n, m = map(int, input().split())
s = []
c = []
for i in range(m):
    si, ci = map(int, input().split())
    s.append(si)
    c.append(ci)
guess = 0
guess1 = []
guess2 = []
guess3 = []
for i in range(m):
    if s[i] == 1:
        guess1.append(c[i])
    elif s[i] == 2:
        guess2.append(c[i])
    else:
        guess3.append(c[i])
guess1 = set(guess1)
guess2 = set(guess2)
guess3 = set(guess3)
guess1 = list(guess1)
guess2 = list(guess2)
guess3 = list(guess3)
existflag = True
if n > 1:
    if len(guess1) > 1 or (0 in guess1):
        existflag = False
if len(guess2) > 1 or len(guess3) > 1:
    existflag = False
if existflag and n == 3:
    guess_100 = 0
    guess_10 = 0
    guess_1 = 0
    if len(guess1) == 0:
        guess_100 = 100
    else:
        guess_100 = guess1[0]*100
    if len(guess2) == 0:
        guess_10 = 0
    else:
        guess_10 = guess2[0]*10
    if len(guess3) == 0:
        guess_1 = 0
    else:
        guess_1 = guess3[0]
    guess = guess_100+guess_10+guess_1
elif existflag and n == 2:
    guess_10 = 0
    guess_1 = 0
    if len(guess1) == 0:
        guess_10 = 10
    else:
        guess_10 = guess1[0]*10
    if len(guess2) == 0:
        guess_1 = 0
    else:
        guess_1 = guess2[0]
    guess = guess_10+guess_1
elif existflag and n == 1:
    if len(guess1) == 1:
        guess = guess1[0]
    else:
        guess = 0
else:
    guess = -1
print(guess)
