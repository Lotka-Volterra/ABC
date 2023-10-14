n = int(input())
a = list(map(int, input().split()))
# 総人口pop
pop = sum(a)
# 総人口が島の数で割り切れないなら、-1を出力
if pop % n != 0:
    print(-1)
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
    print(ans)
