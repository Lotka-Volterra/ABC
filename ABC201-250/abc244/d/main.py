s1, s2, s3 = input().split()
t1, t2, t3 = input().split()
# 1,2,3 あるいは2,3,1あるいは3,1,2の場合Yes
if (s1 == t1 and s2 == t2) or (s1 == t3 and s2 == t1) or (s1 == t2 and s2 == t3):
    print("Yes")
else:
    print("No")
