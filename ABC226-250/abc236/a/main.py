s = input()
a, b = map(int, input().split())
new_s = s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:]
print(new_s)

#リストにすると要素の交換がやりやすい
s = list(input())
a, b = map(int,input().split())
s[a - 1],s[b - 1] = s[b - 1],s[a - 1]
print(''.join(s))