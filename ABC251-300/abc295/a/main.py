wl = ["and", "not", "that", "the", "you"]
n = int(input())
w = list(input().split())
for i in range(n):
    if w[i] in wl:
        print("Yes")
        quit()
print("No")
