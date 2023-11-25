def isKaibun(str):
    # str の長さを取得する
    N = len(str)
    flag=True
    for i in range(N):
        # print(str[i],str[(N - 1) - i])
        if str[i] != str[(N - 1) - i]:
            flag=False
            # print(i)
    # print(flag)
    return flag


n = int(input())

a = []
for i in range(n):
    a.append(input())

for i in range(n - 1):
    for j in range(i+1, n):
        ij = a[i] + a[j]
        ji = a[j] + a[i]
        if isKaibun(ij) or isKaibun(ji):
            # print(ij,isKaibun(ij))
            # print(ji,isKaibun(ji))
            print("Yes")
            quit()
print("No")
