x, y, z = map(int, input().split())
numbers = [x, y, z, 0]
numbers.sort()
xind, yind, zind, ind0 = (
    numbers.index(x),
    numbers.index(y),
    numbers.index(z),
    numbers.index(0),
)
if abs(xind - ind0) == 1:
    print(abs(x))
elif (xind < zind < ind0 and (yind < xind or ind0 < yind)) or (
    xind > zind > ind0 and (yind > xind or ind0 > yind)
):
    print(abs(x))
elif xind < yind < zind < ind0 or xind > yind > zind > ind0:
    print(abs(x))
elif xind < yind < ind0 < zind or xind > yind > ind0 > zind:
    print(abs(x) + abs(z)*2)
else:
    print(-1)
