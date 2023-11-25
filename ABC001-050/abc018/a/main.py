D = []
for i in range(3):
    D.append(int(input()))
E = sorted(D, reverse=True)
for i in D:
    for j in range(3):
        if i == E[j]:
            print(j+1)
