s=list(input())
sl=list(set(s))
if len(sl)==2 and s.count(sl[0])==2:
    print('Yes')
else:
    print('No')
#公式解答例。ソートしてから判定
s.sort()
if s[0]==s[1] and s[1]!=s[2] and s[2]==s[3]:
    print('Yes')
else:
    print('No')