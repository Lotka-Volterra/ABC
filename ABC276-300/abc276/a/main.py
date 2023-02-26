# s = input()
# Aind = -1
# for i in range(len(s)):
#     if s[i] == "a":
#         Aind = i + 1
# print(Aind)

# 後ろから見る
s = input()

for i in range(len(s) - 1, -1, -1):
    if s[i] == "a":
        print(i + 1)
        quit()
print(-1)
