d, t, s = map(int, input().split())
if d/s <= t:
    print('Yes')
else:
    print('No')

# 別解：小数点を使わない方法で計算
if s*t >= d:
    print('Yes')
else:
    print('No')
