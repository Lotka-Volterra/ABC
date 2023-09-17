XY = list(map(int,input().split()))

l = [0, 1, 2]
if XY[0]==XY[1]:
    print(XY[0])
else:
    for i in XY:
        l.remove(i)
    print(l[0])

#別解 ｘとｙの手が別の場合、残る手は３から出た手を引いたもの
x, y = map(int, input().split())
if x==y:
    print(x)
else:
    print(3-x-y)