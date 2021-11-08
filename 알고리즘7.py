arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]

result = list()
for x in arr:
    if x != 2:
       result.append(x)

print(result)