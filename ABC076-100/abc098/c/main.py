n = int(input())
s = input()
w = 0
we = [0]
for i in range(n):
    if s[i] == "W":
        w += 1
    we.append(w)
ans = n
# 累積和を使う。weはその人までの西を向いている人の数。
# 向きを変える必要があるのは、リーダーの左で西を向いている人と、リーダーの右で東を向いている人の数の和
for i in range(1, n + 1):
    attention = we[i - 1] + (n - i - (w - we[i]))
    ans = min(ans, attention)
print(ans)
