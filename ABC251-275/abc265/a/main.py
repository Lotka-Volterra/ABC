x, y, n = map(int, input().split())
if 3 * x <= y:
    print(n * x)
else:
    yans = n // 3
    xans = n - 3 * yans
    print(x * xans + y * yans)
# xansは、nを3で割った余りと考えると、xans=n%3とも書ける