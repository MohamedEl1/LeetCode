def maxsubstringchars():
    s = "aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz"
    count = 1
    maximum = 0

    # iterate through the string and check if the first characters equals the second character
    # if it does then increase count by 1 till they dont equal each other
    # then check if count is greater than the current max value
    # if it is then replace max value with current count and replace count value to 1
    # keep doing that till you finish iterate
    # some edge cases
    # return the max value from either count or maximim (look more into it)
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            count += 1
        else:
            if count > maximum:
                maximum = count
                count = 1
            else:
                count = 1
    if count > maximum:
        maximum = count
    if len(s) == 1:
        return 1
    elif maximum == 0 and s != "":
        return count
    else:
        return maximum

print(maxsubstringchars())
