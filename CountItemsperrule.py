# Count Items Matching a Rule

# Dictionary that counts amount of type, color, and name rule matches
ruleKey = "color"
ruleValue = "blue"

countMatches = {"type": 0, "color": 0, "name": 0}

# List containing items

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]


for i in range(len(items)):

    if ruleKey == "type" and items[i][0] == ruleValue:
        countMatches["type"] = countMatches["type"] + 1

    elif ruleKey == "color" and items[i][1] == ruleValue:
        countMatches["color"] = countMatches["color"] + 1

    elif ruleKey == "name" and items[i][2] == ruleValue:
        countMatches["name"] = countMatches["name"] + 1

print(countMatches[ruleKey])
