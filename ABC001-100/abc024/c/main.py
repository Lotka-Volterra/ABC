n, d, k = map(int, input().split())
L_R = []
for i in range(d):
    l, r = map(int, input().split())
    L_R.append([l, r])
for i in range(k):
    s, t = map(int, input().split())
    current = s
    for j in range(d):
        if L_R[j][0] <= current <= L_R[j][1]:
            if L_R[j][0] <= t <= L_R[j][1]:
                print(j + 1)
                break
            elif current > t:
                current = L_R[j][0]
            else:
                current = L_R[j][1]
