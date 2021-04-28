
s = "1326#"
result = ""
i = 0
lengthOfString = len(s)

while i < lengthOfString:
    if i + 2 < lengthOfString and s[i + 2] == '#':
        result = result + chr(int(s[i:i + 2]) + 96)
        i = i + 3
    else:
        result = result + chr(int(s[i]) + 96)
        i = i + 1
print(result)