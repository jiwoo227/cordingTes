arr = [1,4,2,3]

# 역순 = [0] * 4
#
# 역순[3] = arr[0]
# 역순[2] = arr[1]
# 역순[1] = arr[2]
# 역순[0] = arr[3]

reversed_arr= [0] * len(arr)

length = len(arr)

for i in range(length):
    reversed_arr[length-i+1] = arr[i]

# 역순[맥스-1] = arr[0]
# 역순[맥스-2] = arr[1]
# 역순[맥스-3] = arr[2]
# 역순[맥스-4] = arr[3]

print(reversed_arr)