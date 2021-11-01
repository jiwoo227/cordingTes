arr = [8,5,6,3,4]

for i in range(0, len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[i]