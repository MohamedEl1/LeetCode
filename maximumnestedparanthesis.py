# Go through string and count the paranthesis
# count the parantheses if ( then +1 if ) then -
# create another variable called max num and update it with count value if count > max num
values = dict()
s = "(1+(2*3)/((2)-1))"
count = 0
max_num = 0

for i in s:
    if i == '(':
        count = count + 1
    elif i == ')':
        count = count - 1

    # this basically keeps tracks of the maximum nested paranthesis, and returns the maximum nested paranthesis
    if count > max_num:
        max_num = count
print(max_num)