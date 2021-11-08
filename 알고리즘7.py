arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]

새로운공간 = list()
for x in arr:
    if x != 2:
        새로운공간.append(x)

print(새로운공간)