p, q, r = map(int, input().split())
print(min(p+q, q+r, r+p))
# 別海
print(p+q+r-max(p, q, r))
