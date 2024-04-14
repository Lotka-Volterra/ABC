s = list(input())
n = len(s)
is_kaibun = True
# まずs自体で回文かどうか判定する
for i in range(n // 2):
    if s[i] != s[-i - 1]:
        is_kaibun = False
        break
if is_kaibun:
    print("Yes")
    quit()
# sの先頭および末尾のaを数える。
# sの先頭のa>末尾のaであれば、どうやっても回文にできない
# 上記以外の場合、先頭および末尾から連続するaを除いた文章について回文判定を行う
new_s = s
front_a = 0
if s[0] == "a":
    i = 0
    while i < n:
        if s[i] != "a":
            break
        i += 1
    front_a += i + 1
    new_s = s[i:]
new_s = "".join(list(reversed(new_s)))
# print(new_s)
back_a = 0
if new_s[0] == "a":
    i = 0
    while i < len(new_s):
        if new_s[i] != "a":
            break
        i += 1
    back_a += i + 1
    # print(i)
    new_s = new_s[i:]
# print(new_s)
if front_a > back_a:
    print("No")
    quit()
is_kaibun = True
for i in range(len(new_s) // 2):
    if new_s[i] != new_s[-i - 1]:
        is_kaibun = False
        break
if is_kaibun:
    print("Yes")
    quit()
print("No")
