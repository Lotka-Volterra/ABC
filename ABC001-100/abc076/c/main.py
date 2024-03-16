s = list(input())
t = input()
ans = []
for i in range(len(s) - len(t) + 1):
    restorable = True
    for j in range(len(t)):
        if s[i + j] != "?" and s[i + j] != t[j]:
            restorable = False
            break
    if restorable:
        ans_str = ""
        for j in range(i):
            ans_str = ans_str + "a" if s[j] == "?" else ans_str + s[j]
        ans_str += t
        for j in range(i + len(t), len(s)):
            ans_str = ans_str + "a" if s[j] == "?" else ans_str + s[j]
        ans.append(ans_str)
ans.sort()
print(ans[0]) if len(ans) != 0 else print("UNRESTORABLE")
