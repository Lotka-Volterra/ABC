import math
# 回答例、出力生成用に使用
a,b,w=map(int,input().split())
upper=int(math.floor(1000*w/a))
lower=int(math.ceil(1000*w/b))

if lower>upper:
  print("UNSATISFIABLE")
else:
  print(lower,upper)
