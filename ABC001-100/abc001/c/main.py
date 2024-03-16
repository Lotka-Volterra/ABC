deg, dis = map(int, input().split())
dir = "N"
w = 0
deg *= 10
# deg<1125がNEの分岐に入ってしまうバグがあったため、修正。
if deg < 1125:
    dir = "N"
elif deg < 3375:
    dir = "NNE"
elif deg < 5625:
    dir = "NE"
elif deg < 7875:
    dir = "ENE"
elif deg < 10125:
    dir = "E"
elif deg < 12375:
    dir = "ESE"
elif deg < 14625:
    dir = "SE"
elif deg < 16875:
    dir = "SSE"
elif deg < 19125:
    dir = "S"
elif deg < 21375:
    dir = "SSW"
elif deg < 23625:
    dir = "SW"
elif deg < 25875:
    dir = "WSW"
elif deg < 28125:
    dir = "W"
elif deg < 30375:
    dir = "WNW"
elif deg < 32625:
    dir = "NW"
elif deg < 34875:
    dir = "NNW"
if dis >= 1959:
    w = 12
elif dis >= 1707:
    w = 11
elif dis >= 1467:
    w = 10
elif dis >= 1245:
    w = 9
elif dis >= 1029:
    w = 8
elif dis >= 831:
    w = 7
elif dis >= 645:
    w = 6
elif dis >= 477:
    w = 5
elif dis >= 327:
    w = 4
elif dis >= 201:
    w = 3
elif dis >= 93:
    w = 2
elif dis >= 15:
    w = 1
else:
    w = 0
    dir = "C"
print(dir, w)
