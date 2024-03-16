from collections import defaultdict

num = defaultdict(int)
n, k = map(int, input().split())
count = 0
num_list = set()
for i in range(n):
    a, b = map(int, input().split())
    num[a] += b
    num_list.add(a)
num_list = sorted(list(num_list))
for i in num_list:
    if count < k <= count + num[i]:
        print(i)
        quit()
    count += num[i]
