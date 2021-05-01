# 832. Flipping an Image
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.


image = [[1,1,0],[1,0,1],[1,0,0]]
imagetwo = []

# reverse each list within a list
for i in range(len(image)):
    imagetwo.append(image[i][::-1])

# replace all 0's with 1's and 1's with 0's

for i in range(len(imagetwo)):
    for j in range(len(imagetwo)):
        if imagetwo[i][j] == 0:
            imagetwo[i][j] = 1
        else:
            imagetwo[i][j] = 0


print(imagetwo)