o = input()
e = input()
ans = ""
for i in range(len(o) - 1):
    ans += o[i] + e[i]
ans += o[-1]
if len(e) == len(o):
    ans += e[-1]
print(ans)
