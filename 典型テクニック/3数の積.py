# ABC227 C
# A<=B<=Cとして、A*B*C<=Nとなる組み合わせの数を求める問題。
# 浮動小数点演算の誤差でWAになった。
# たとえば、Aの範囲をmath.ceil(N**(1/3))で求めると、N=64のとき、math.ceil(N**(1/3))は3と計算されてしまった。
# 小数の計算を、整数の計算で代用するのがポイント。
# n乗根を計算して比較するのではなく、n乗を計算して比較するように切り替えると誤差を考えずに済む
N = int(input())
ans = 0
for a in range(1, N + 1):
    if a * a * a > N:
        break
    for b in range(a, N + 1):
        if a * b * b > N:
            break
        ans += N // a // b - b + 1
print(ans)
