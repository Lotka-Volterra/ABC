s1 = input()
s2 = input()
s1black = s1.count('#')
s2black = s2.count('#')
if s1black+s2black >= 3:
    print('Yes')
elif s1black == 2 or s2black == 2 or s1[0] == s2[0]:
    print('Yes')
else:
    print('No')

#公式回答。答えがNoになるのは以下の2通りしかない。
# .#  #.
# #.  .#
s1=input()
s2=input()
if (s1=='.#' and s2=='#.') or (s1=='#.' and s2=='.#'):
    print('No')
else:
    print('Yes')