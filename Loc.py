string = "ILOVEKFRLOVEE"

find = "LOV"
print(string.count(find))
count = 0
for i in range(len(string)):
    if string[i] == find[0] and i+len(find) <= len(string):
        if string[i+1] == find[1]:
            if string[i+2] == find[2]:

                count +=1