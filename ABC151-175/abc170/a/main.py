x=list(map(int,input().split()))
print(x.index(0)+1)

#1から5までの和が15だから、何が0になってるかは入力値の総和を引けばわかる
print(15 - sum(list(map(int, input().split()))))