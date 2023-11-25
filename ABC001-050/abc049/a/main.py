s = input()
vowel = ["a", "i", "u", "e", 'o']
if s in vowel:
    print("vowel")
else:
    print("consonant")

#別解
c=input()
if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
    print("vowel")
else:
    print("consonant")

#わざわざリスト使わなくても
s = input()
vowel = "aiueo"
if s in vowel:
    print("vowel")
else:
    print("consonant")
