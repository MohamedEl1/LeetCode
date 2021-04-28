
counting = {"R":0, "L":0}
balanced_strings = []
s = "RLRRLLRLRL"
result = ""

# iterate through the characters in s
for i in s:
    # check if character is either R or L and increment the count of character and add it to the string
    if i == "R":
        counting["R"] = counting["R"] + 1
        result = result + i
    elif i == "L":
        counting["L"] = counting["L"] + 1
        result = result + i
    # if the count of R and L are equal then we found a balanced string, append to the list of balanced strings and empty result and redo till we have all balanced strings
    if counting["R"] == counting["L"]:
        balanced_strings.append(result)
        result = ""

# its not removing previous strings

print(balanced_strings)




print(s.count("R") == s.count("L"))