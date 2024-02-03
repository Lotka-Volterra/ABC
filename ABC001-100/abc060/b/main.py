a, b, c = map(int, input().split())
amari = a % b
for i in range(1, 101):
    if amari*i % b == c:
        print('YES')
        quit()
print('NO')

# 愚直に101まで全探索したが、実際はもっと少なくて済む
# (k+b)*a % b <-> (k*a+b*a) % b <-> k*a % b
# より、余りは1*aからb*aを繰り返す。よって、1*aからb*aについて、余りがcになるか全探索すればいい
a, b, c = map(int, input().split())
amari = a % b
for i in range(1, b):
    if a*i % b == c:
        print('YES')
        quit()
print('NO')
