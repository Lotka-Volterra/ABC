n = int(input())
C, S, F = [], [], []
for i in range(n - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)
for i in range(n):
    if i == n - 1:
        print(0)
        quit()
    time = C[i] + S[i]
    for j in range(i + 1, n - 1):
        # 始発より前に到着した場合、始発を待つ
        if time <= S[j]:
            time = S[j] + C[j]
        else:
            diff = (time - S[j]) % F[j]
            # 到着と同時に出発
            if diff == 0:
                time += C[j]
            else:
                # 到着してから(F[j] - diff)だけ待ってから出発
                time += (F[j] - diff) + C[j]
    print(time)
