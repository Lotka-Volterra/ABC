n = int(input())
a = list(map(int, input().split()))
bina = []
for i in range(n):
    bina.append(bin(a[i]))
# 左シフトが何回できるか
for i in range(30):
    for j in range(n):
        if bina[j][-1 - i] != "0":
            print(i)
            quit()
