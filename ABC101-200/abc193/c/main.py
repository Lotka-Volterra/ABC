n = int(input())
expressed = set()
# a**bとして表される数を列挙し、全体から引く
for i in range(2, n + 1):
    # sqrt(n)以上は調べる必要がない
    if i**2 > n:
        break
    # 2**33<10**100<2**34より、最大でも33まで調べれば良い
    for k in range(2, 34):
        if i**k > n:
            break
        expressed.add(i**k)
print(n - len(expressed))
