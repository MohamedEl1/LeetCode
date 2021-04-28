s = "friend"

t = "family"

s1 = list(s)

t1 = list(t)


for i in range(len(s1)):
    for j in range(len(t1)):
        if s1[i] == t1[j]:
            s1[i] = ""
            t1[j] = ""

result =  "".join(s1)
print(len(result))


# second approach that covers all test cases
s1 = {}
t1 = {}

# count each character in s and t
for i in s:
    if i in s1:
        s1[i] = s1[i] + 1
    else:
        s1[i] = 1

for i in t:
    if i in t1:
        t1[i] = t1[i] + 1
    else:
        t1[i] = 1

# now substract the count from characters in s and t and return the total missing chars
# I learnt to substract two dictionary values from each other
# I also learn that the dicitonary get method has an extra parameter for a default value if a key/value does not exist in the dictionary
missing = 0

for i in s1:
    diff = s1.get(i, 0) - t1.get(i, 0)
    if diff > 0:
        missing = missing + diff
print(missing)
