a,b =input().split()
ab = int(a+b)
heiho = "No"
for i in range(4,317):
    if ab == i**2:
        heiho = "Yes"
        break
print(heiho)

#317は、100100の平方根が316.3...だったので。
# ただ、これはいちいち計算するより、高々1000*1000未満と割り切って1000までにしてもいい
#別解。1/2乗が切り捨てた1/2乗と一致するか
a, b = input().split()
p = int(a + b)
if p ** 0.5 == int(p ** 0.5):
    print("Yes")
else:
    print("No")