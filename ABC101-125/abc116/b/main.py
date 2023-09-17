s = int(input())
a = []
a.append(s)
for i in range(1, 1000000):
    ai = 0
    if a[i-1] % 2 == 1:
        ai = 3*a[i-1]+1
    else:
        ai = a[i-1]//2
    if ai in a:
        print(i+1)
        quit()
    a.append(ai)

# set型を使って、前の項だけ変数に保存しておく
s = int(input())
a = set([s])
mae = s
for i in range(1, 1000000):
    if mae % 2 == 1:
        mae = 3*mae+1
    else:
        mae = mae//2
    if mae in a:
        print(i+1)
        quit()
    a.add(mae)
