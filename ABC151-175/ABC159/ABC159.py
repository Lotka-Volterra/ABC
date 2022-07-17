# ｎC２とｍC2の和
n, m = map(int, input().split())
even = max(m*(m-1)//2, 0)
odd = max(n*(n-1)//2, 0)
print(odd+even)

#０が入るとm*(m-1)//2は０が分子にあるので０になる。Maxは必要ない