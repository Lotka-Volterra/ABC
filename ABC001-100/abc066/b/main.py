s=input()
lens=len(s)
maxlen=0
for i in range(2,lens,2):
    if s[:(lens-i)//2]==s[(lens-i)//2:lens-i]:
        maxlen=lens-i
        break
print(maxlen)

#書き直すなら
s=input()
lens=len(s)
maxlen=0
for i in range(2,lens,2):
    if s[:(lens-i)//2]==s[(lens-i)//2:lens-i]:
        print(lens-i)
        quit()
#別解
s = input()[:-1]

while True:
    if len(s) % 2 == 0:
        if s[:len(s)//2] == s[len(s)//2:]:
            print(len(s))
            break
    s = s[:-1]