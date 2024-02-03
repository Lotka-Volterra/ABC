import math

a, b, h, m = map(float, input().split())
# 短針を長針の時間軸に直すと、1分で1/12分の角度だけ動く
tanshin = 5 * h + 1 / 12 * m
# tanshin = 60 * h + m
# choshin = 12 * m
# diff = abs(tanshin - choshin)
# 短針と長針の間の分の差を求める
diff = abs(tanshin - m)
# angle = min(diff, 720 - diff) / 2
# 分の差を角度（度数法）に戻す
angle = min(diff, 60 - diff) * 6
# print(angle)
# print(math.radians(angle))
# print(math.cos(math.radians(angle)))
# print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle)))
# math.radiansで角度をラジアン(弧度法)に変換してから、余弦定理
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle))))
