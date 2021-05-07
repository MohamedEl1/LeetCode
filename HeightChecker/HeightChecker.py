# Program that checks the height that is not in order and count them


heights = [1,2,3,4,6,5]

expected = heights.copy()
expected.sort()

count = 0
for i in range(len(expected)):
    if heights[i] != expected[i]:
        count+=1



print(count)