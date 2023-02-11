a, b = map(int, input().split())
if abs(a-b) == 1:
    print("Yes")
elif (a == 1 and b == 10) or (a == 10 and b == 1):
    print("Yes")
else:
    print("No")

#b>aなので、b-a==1 or b-a==9で判定できる  