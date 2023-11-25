s = input()
ans = [[0, ""]]
if len(s) > 1:
    for i in range(len(s)):
        for j in range(i + 1, len(s)+1):
            target = s[i : j]
            for k in range(len(target)):
                if target[k] not in "ATGC":
                    break
                if k == len(target) - 1:
                    ans.append([len(target), target])
else:
    if s in "ATGC":
        print(1)
        quit()
ans.sort(reverse=True)
print(ans[0][0])
