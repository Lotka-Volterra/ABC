a, b = map(int, input().split())
if a*b % 2 == 0:
    print("No")
else:
    print("Yes")
# Trueは１と等価なので、
if a*b % 2:
    print("Yes")
else:
    print("No")
#実装する
for i in range(1,4):
    if a*b*i%2:
        print("Yes")
        exit()
print("No")    

