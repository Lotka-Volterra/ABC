n = int(input())
X, Y, H = [], [], []
undefined_X, undefined_Y, undefined_H = [], [], []
for i in range(n):
    x, y, h = map(int, input().split())
    # 方針:hi==0の場合、x,y,hを数式で確定できないため別枠にする
    if h == 0:
        undefined_X.append(x)
        undefined_Y.append(y)
        undefined_H.append(h)
    else:
        X.append(x)
        Y.append(y)
        H.append(h)
for cx in range(101):
    for cy in range(101):
        h_list = set()
        for i in range(len(X)):
            h_list.add(H[i] + abs(X[i] - cx) + abs(Y[i] - cy))
        if len(h_list) != 1:
            continue
        # cx,cyを全探索してhを確定させる
        temp_h = list(h_list)[0]
        is_ok = True
        # hi==0となるxi,yiについて検証する
        for i in range(len(undefined_X)):
            if (
                max(temp_h - abs(undefined_X[i] - cx) - abs(undefined_Y[i] - cy), 0)
                != 0
            ):
                is_ok = False
                break
        if is_ok:
            print(cx, cy, temp_h)
            exit()
