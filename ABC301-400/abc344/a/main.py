S = input()
ans = ""
bar_found = False
for i in S:
    if i == "|":
        if bar_found:
            bar_found = False
        else:
            bar_found = True
    if not bar_found and i != "|":
        ans += i
print(ans)
