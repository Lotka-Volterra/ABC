h, w = map(int, input().split())
S = [list(input()) for i in range(h)]
T = [list(input()) for i in range(h)]

row_S = [[""] * h for i in range(w)]
row_T = [[""] * h for i in range(w)]
for i in range(w):
    for j in range(h):
        row_S[i][j] = S[j][i]
        row_T[i][j] = T[j][i]
string_S = []
string_T = []
for i in range(w):
    string_S.append("".join(row_S[i]))
    string_T.append("".join(row_T[i]))
string_S.sort()
string_T.sort()
for i in range(w):
    if string_S[i] != string_T[i]:
        print("No")
        quit()
print("Yes")
