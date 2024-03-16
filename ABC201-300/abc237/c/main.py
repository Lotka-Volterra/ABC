s = list(input())
n = len(s)
is_kaibun = True
for i in range((n - 1) // 2):
    if s[i] != s[-i - 1]:
        is_kaibun = False
        break
if is_kaibun:
    print("Yes")
    quit()
for i in range(n - 1, -1, -1):
    if s[i] != "a":
        break
    is_Kaibun = True
    for j in range((i - 1) // 2):
        if s[j] != s[i - 1 - j]:
            is_Kaibun = False
    if is_Kaibun:
        print("Yes")
        quit()
print("No")
