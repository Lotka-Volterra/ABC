def my_ans(deg, dis):
    dir = "N"
    w = 0
    deg *= 10
    if 1125 <= deg < 3375:
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
    return [dir, w]


def ans(deg, dis):
    k = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
        "N",
    ]
    h = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6, 300]
    dis = round(dis / 60 + 0.001, 1)
    for i in range(17):
        if deg < 112.5 + 225 * i:
            break
    for j in range(13):
        if dis <= h[j]:
            break
    return [k[i] if j else "C", j]


for deg in range(3600):
    for dis in range(12000):
        my_ans_list = my_ans(deg, dis)
        your_ans_list = ans(deg, dis)
        if my_ans_list[0] != your_ans_list[0] or my_ans_list[1] != your_ans_list[1]:
            print("-----")
            print(deg, dis)
            print(my_ans_list)
            print(your_ans_list)
            print("-----")
            break
