words = ["mass", "as", "hero", "superhero"]

result = []

for i in words:
    for j in words:
        if i in j and i != j:
            result.append(i)

print(result)
