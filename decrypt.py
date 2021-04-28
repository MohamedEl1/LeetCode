# create a dictionary that holds key value pairs of alphabet to integer
# create an empty string
# iterate through the values list and match the element in values with the key in the dictionary and add the value of the key to the string created

integer_to_alphabet = {'1': 'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10#':'j', '11#': 'k', '12#':'l', '13#':'m', '14#':'n', '15#':'o', '16#':'p', '17#':'q', '18#':'r', '19#':'s', '20#':'t','21#':'u', '22#':'v', '23#':'w', '24#':'x', '25#':'y', '26#':'z'}
values = []

s = "10#11#12"
#s = "1326#"
result = ""
while '#' in s:
    d = s.find('#')
    substring = s[d-2:d+1]
    #values.extend(list(s[:d - 2]))
    #values.append(substring)
    result = result + integer_to_alphabet[substring]
    result = result + integer_to_alphabet[s[:d - 2]]
    s = s.replace(substring, "")
    s = s.replace(s[:d-2], "")
#values.extend(list(s))

#for i in values:




print(result)
# print(d)
# print(substring)
print(values)
print(list(s))
print(values)

