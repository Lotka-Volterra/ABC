n = int(input())
h = list(map(int, input().split()))
count = 0
tsuduki = False
# 高さが1以上の部分が続く箇所の数を数える
for i in range(max(h)):
    for j in range(n):
        if h[j] > 0:
            if not tsuduki:
                count += 1
                tsuduki = True
            # 花壇の端なら続きフラグをfalse
            if j == n - 1:
                tsuduki = False
            h[j] -= 1
        else:
            tsuduki = False
print(count)
