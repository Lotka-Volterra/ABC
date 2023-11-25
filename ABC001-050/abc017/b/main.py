X = input()
choku = "YES"

while len(X)>0:
    if X[-2:]=="ch":
        X = X[:-2]
        continue
    elif X[-1]=="o" or X[-1]=="k" or X[-1]=="u":
        X = X[:-1]
        continue
    else:
        choku = "NO"
        break
print(choku)
