n = int(input())
h = list(map(int, input().split()))
h[0] -= 1
for i in range(1, n):
    if h[i] > h[i-1]:
        h[i] -= 1
    elif h[i] < h[i-1]:
        print('No')
        quit()
print('Yes')
#https://img.atcoder.jp/abc136/editorial.pdf
#「∀i.Hi ≥ Mi − 1 ⇔ 答えは Yes」