n = int(input())
l = list(map(int, input().split()))
l.sort()
ruiseki = [0] * (10**3 + 1)
for i in range(n):
    ruiseki[l[i]] += 1
ruisekiwa = [0]
for i in range(10**3):
    ruisekiwa.append(ruisekiwa[i] + ruiseki[i + 1])
ans = 0
# print(ruisekiwa)
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        # a<=b<=cとすると、cはb<=c<a+b
        # cの候補の数を考える
        c_candidate = ruisekiwa[min(l[a] + l[b], 10**3 + 1) - 1] - ruisekiwa[l[b] - 1]
        # cの候補の範囲内に、aあるいはbが含まれていれば、取り除く
        if l[b] - 1 < l[a] < l[a] + l[b]:
            c_candidate -= 1
        if l[b] - 1 < l[b] < l[a] + l[b]:
            c_candidate -= 1
        ans += c_candidate
print(ans)
