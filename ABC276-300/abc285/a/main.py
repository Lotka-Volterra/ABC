a, b = map(int, input().split())
ans = 0
if a == 1 and (b == 2 or b == 3):
    ans = 1
elif (a == 2 or a == 3) and (b == 2 * a or b == 2 * a + 1):
    ans = 1
elif (4 <= a <= 7) and (b == 2 * a or b == 2 * a + 1):
    ans = 1
print(["No", "Yes"][ans])

# 今回は、a=b//2（切り捨て（FLOOR関数））であれば
a,b=map(int,input().split())
if a==b//2:
  print("Yes")
else:
  print("No")
