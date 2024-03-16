n, q = map(int, input().split())
othello = [0] * (n + 1)
for i in range(q):
    l, r = map(int, input().split())
    othello[l - 1] += 1
    othello[r] -= 1
othello[0] %= 2
for i in range(1, n):
    othello[i] = (othello[i] + othello[i - 1]) % 2
print("".join(map(str, othello[:-1])))
