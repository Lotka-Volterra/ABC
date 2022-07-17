k = int(input())
if k % 2 == 0:
    even = k//2
    print(even**2)
else:
    even = (k-1)//2
    print(even*(even+1))
# 偶数は、[k/2]つまり、kを2で割った商（切り捨て）。奇数は、k-偶数の数。
k = int(input())
even = k//2
print((k-even)*even)
