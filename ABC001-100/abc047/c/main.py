s = input()
before_string = s[0]
compressed_string = s[0]
for i in range(1, len(s)):
    if s[i] != before_string:
        compressed_string += s[i]
        before_string = s[i]
print(len(compressed_string) - 1)
