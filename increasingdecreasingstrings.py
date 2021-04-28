#
# alreadychosensmallest = set()
# alreadychosenbiggest = set()
# for i in range(len(s)):
#     for j in range(len(s)):
#         if s[j] < s[i] and s[j] not in alreadychosensmallest:
#             result = result + s[j]
#             alreadychosensmallest.add(s[j])
#
# for i in range(len(s)):
#     for j in range(len(s)):
#         if s[j] > s[i] and s[j] not in alreadychosenbiggest:
#             result = result + s[j]
#             alreadychosenbiggest.add(s[j])

# while there is something in s
s = "rat"
s = list(s)
result = []
# keep looping till list s is empty
while s:
    temp_list = set(s) # converts list to set and removes duplicates
    temp_list = sorted(temp_list) # sorts the set alphabetical order
    for i in temp_list:
        result.append(i) # append the result of sorted set (smallest to largest character)
        s.remove(i) # remove the character appended from the string

        # do the same thing as above but from largest to smallest character

    temp_list = set(s)
    temp_list = sorted(temp_list, reverse=True)
    for i in temp_list:
        result.append(i)
        s.remove(i)
# join the characters together to form a string and return it
print(''.join(result))

#
#
# print(s)
#
#
# print(result)

# if


word1 = "abc"
word2 = "pqr"
result = ""
numba = 0
if len(word1) < len(word2):
    numba = len(word1)
else:
    numba = len(word2)

for i in range(numba):
    result = result + word1[i]
    result = result + word2[i]

# check which string is larger and append the rest of the largest string characters from the length of the smallest string above
# if statement to check which is larger
# for loop to append the rest

if len(word1) > len(word2):
    for i in range(numba, len(word1)):
        result = result + word1[i]
else:
    result = list(result)
    ans = word2[numba:]
    result.append(ans)
    result = "".join(result)



print(result)



#print(numba)