a, b, w = map(int, input().split())
# 最大値は切り捨て（小数の個数のみかんはない、切り捨てても条件を満たす）
maxOrange = (w*1000)//a
# 最小値は切り上げ（切り上げないと条件を満たさない）
minOrange = (w*1000+(b-1))//b
if maxOrange >= minOrange:
    print(minOrange, maxOrange)
else:
    print('UNSATISFIABLE')
