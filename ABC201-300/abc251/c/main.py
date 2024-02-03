from collections import defaultdict

n = int(input())
num = defaultdict(int)
st = []
for i in range(n):
    s, t = input().split()
    if num[s] == 0:
        st.append([10**9 - int(t), i + 1])
    num[s] += 1
st.sort()
print(st[0][1])
