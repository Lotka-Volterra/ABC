N = input()
for i in range(2):
    if int(N[i:i+3]) % 111 == 0:
        print("Yes")
        exit()
print("No")

#別解
a = list(map(int,input().split()))

for x in range(2):
    if a[x] == a[x+1]:
        if a[x+1] == a[x+2]:
            print("Yes")
            exit()

print("No")