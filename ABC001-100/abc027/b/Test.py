# n = int(input())
# a = list(map(int, input().split()))


def wrongAnswer(n, a):
    # 総人口pop
    pop = sum(a)
    # 総人口が島の数で割り切れないなら、-1を出力
    if pop % n != 0:
        return -1
    else:
        # 左側の島から端をかけていく。
        # 左側の島と橋が繋がっているかどうかのフラグ
        bridgeFlag = False
        # 橋で繋がっている島の総人口
        tempPop = 0
        # 一つの島あたりの人口
        averagePop = pop // n
        # 橋で繋がっている島の数（初期値は、橋が繋がっていない状態＝１）
        islandCount = 1
        # かける橋の数の合計
        ans = 0
        # すべての島について判定
        for i in range(n):
            # 橋が繋がっているとき
            if bridgeFlag:
                # 橋で繋がっている島の数およびその島上の総人口を更新
                tempPop += a[i]
                islandCount += 1
                # 総人口が、島一つあたりの平均人口*島の数になれば、もう橋をかける必要がない
                # modを取らないのは、島一つあたりの平均人口=1の場合を考慮
                if tempPop == averagePop * islandCount:
                    # 橋フラグと、島カウントを初期化
                    bridgeFlag = False
                    islandCount = 1
                else:
                    # まだ橋をかける必要があるので、橋の数を更新
                    ans += 1
            # 橋がかかっていない状態
            else:
                # その島の人口が、島一つあたりの平均人口ではない場合、橋をかける必要がある
                if a[i] != averagePop:
                    tempPop += a[i]
                    bridgeFlag = True
                    ans += 1
        return ans


def mohanKaito(n, a):
    n = int(input())
    a = list(map(int, input().split()))
    # 総人口pop
    pop = sum(a)
    # 総人口が島の数で割り切れないなら、-1を出力
    if pop % n != 0:
        return -1
    # 一つの島あたりの人口
    averagePop = pop // n
    popSum = [a[0]]
    for i in range(1, n):
        popSum.append(popSum[i - 1] + a[i])
    ans = 0
    for i in range(n - 1):
        if popSum[i] != averagePop * (i + 1):
            ans += 1
    return ans


for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if mohanKaito(4, [i, j, k, l]) != wrongAnswer(4, [i, j, k, l]):
                    print(i, j, k, l)

# 結局目で見てバグを見つけたが、tempPop += a[i]の部分が問題。tempPopを初期化できていない
# WAになるのは、途中で橋をかけるのをやめて、その後再度橋をかけるとき。
# 橋をかけ直す回数が複数ある入力だとWAになるはず。
# 出力例2は初期化できていなくても問題ない（偶然答えが出る）入力だった
