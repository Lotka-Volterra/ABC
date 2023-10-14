n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
# 最強はbに現れない。最強が特定できるときは、n-1人の敗者の情報がbにある。
if len(b) != n - 1:
    print(-1)
else:
    for i in range(1, n + 1):
        # bに現れないのが、最強の候補
        if i not in b:
            print(i)
            quit()
