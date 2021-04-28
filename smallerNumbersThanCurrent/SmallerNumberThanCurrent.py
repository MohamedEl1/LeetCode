
# Program that returns a list of numbers that count the smaller numbers than the current

# Algoritm
# Nested for loop i and j for comparision
# Check if i is not equal to j and check if j is less than i
# if it is then increment count
# append count to a list then reset count to 0
# return the list

nums = [8,1,2,2,3]
count = 0
result = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[j] != nums[i] and nums[j] < nums[i]:
            count += 1
    result.append(count)
    count = 0

print(result)