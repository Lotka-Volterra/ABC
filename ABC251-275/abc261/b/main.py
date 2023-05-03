n = int(input())
result = []
for i in range(n):
    a = list(input())
    result.append(a)
for i in range(n):
    for j in range(i + 1, n):
        if result[i][j] == "W" and result[j][i] != "L":
            print("incorrect")
            quit()
        elif result[i][j] == "L" and result[j][i] != "W":
            print("incorrect")
            quit()    
        elif result[i][j] == "D" and result[j][i] != "D":
            print("incorrect")
            quit()
print("correct")
