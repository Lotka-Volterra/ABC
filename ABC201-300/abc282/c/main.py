n = int(input())
s = list(input())
# kukuri = []
# for i in range(n):
#     if s[i] == '"':
#         kukuri.append(i)
# kukuri_kukan = []
# for i in range(len(kukuri) // 2):
#     kukuri_kukan.append([kukuri[i * 2], kukuri[i * 2 + 1]])
# for i in kukuri_kukan:
#     for j in range(i[0], i[1] + 1):
#         if s[j] == ",":
#             s = s[:j] + "*" + s[j + 1 :]
# s = s.replace(",", ".")
# s = s.replace("*", ",")
flag = True
for i in range(n):
    if s[i] == '"':
        flag = not flag
    elif s[i] == "," and flag:
        s[i] = "."

print("".join(s))
