nums = [1,2,3,4,4,3,2,1]
n = 4
#n = 3

# Divide the array into the n amount specified
secondArray = nums[n:]
firstArray = nums[:n]

thirdArray = []

print(firstArray)
print(secondArray)

# now iterate through the second array and append each element every second time in first array

for i in range(len(secondArray)):
    thirdArray.append(firstArray[i])
    thirdArray.append(secondArray[i])

print(thirdArray)