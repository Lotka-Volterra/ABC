from collections import defaultdict

n = int(input())
v = list(map(int, input().split()))
odd = defaultdict(int)
even = defaultdict(int)
odd[0] = 0
even[0] = 0
for i in range(n):
    if i % 2 == 0:
        even[v[i]] += 1
    else:
        odd[v[i]] += 1
odd_list = [[v, k] for k, v in odd.items()]
even_list = [[v, k] for k, v in even.items()]
odd_list.sort(reverse=True)
even_list.sort(reverse=True)
ans = 0
if odd_list[0][1] != even_list[0][1]:
    ans += n - (even_list[0][0] + odd_list[0][0])
else:
    if odd_list[0][0] > even_list[0][0]:
        ans += n - (odd_list[0][0] + even_list[1][0])
    elif odd_list[0][0] < even_list[0][0]:
        ans += n - (odd_list[1][0] + even_list[0][0])
    else:
        ans += n - (odd_list[0][0] + max(odd_list[1][0], even_list[1][0]))
print(ans)
