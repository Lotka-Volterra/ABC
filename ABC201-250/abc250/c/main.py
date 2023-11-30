n, q = map(int, input().split())
# ボールの番号から位置を対応させる
ball = list(range(n + 1))
# 位置からボールの番号を対応させる
position = list(range(n + 1))
for i in range(q):
    x = int(input())
    ballpos = ball[x]
    nextballpos = ballpos + 1
    if ballpos == n:
        nextballpos = ballpos - 1
    ball[x] = nextballpos
    ball[position[nextballpos]] = ballpos
    position[ballpos] = position[nextballpos]
    position[nextballpos] = x
print(*position[1:])
