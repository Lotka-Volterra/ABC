N = int(input())
n = N//2
if N % 2 == 0:
    print(n)
else:
    print(n+1)

#別解　切り上げ（つまり、偶数なら２で割った時の商を出し、奇数なら２で割った時の商＋１を出す）
a=int(input())
print((a+1)//2)