x, k, d = map(int, input().split())
# まず、絶対値を最小にする方向に進む
# 進んでからさらに回数が残っている場合(この時の位置xについて、abs(x)<d)
# 残っている回数が偶数回なら、この時の位置xを出力（偶数回の移動で往復してxに戻る）
# 残っている回数が奇数回なら、abs(x)<dより、1回0を越えて移動したら絶対値が最小になり、そこから往復を繰り返していればいい
sho = abs(x) // d
if sho > k:
    print(abs(x) - d * k)
else:
    x = abs(x) - d * sho
    if (k - sho) % 2:
        print(abs(x - d))
    else:
        print(x)
