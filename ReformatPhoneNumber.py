# Program the reformats given phone number
# 1. Remove dashes and white space from given phone number
# 2. if the length of the phone number is greater than 4 then add numbers in blocks of 3 by using a while loop and incrementing count by 3 every 3 blocks till there 4 or less numbers
# 3. after that get out of the while loop, and check if the length of numbers left is equal to 4 or 3 or 2
# 4. if the length of numbers left is equal to 4 then split the the numbers left into two numbers each and increment the result with dashs
# if length is 3 then add the rest of numbers to result
# if length is 2 then add the rest of numbers to result

phoneNumber = "123 4-5678"
s = ""

phoneNumber = phoneNumber.replace(" ", "")
phoneNumber = phoneNumber.replace("-", "")

count = 0

while len(phoneNumber[count:]) > 4:
    s += phoneNumber[count:count+3]
    s += "-"
    count += 3


if len(phoneNumber[count:]) == 4:
            temp = phoneNumber[count:]
            s = s + phoneNumber[count:-2]
            s = s + "-"
            count += 2
            s = s + phoneNumber[count:]
            count += 2
elif len(phoneNumber[count:]) == 3:
            s = s + phoneNumber[count:]
elif len(phoneNumber[count:]) == 2:
            s = s + phoneNumber[count:]



print(phoneNumber)
print(s)
print(len(phoneNumber[:]))