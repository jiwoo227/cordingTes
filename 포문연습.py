arr = [2,3,7,1]

#최소값 구하기
최소값 = arr[0]
for x in arr:
    if x < 최소값:
        최소값 = x

최댓값 = arr[0]
for x in arr:
    if x > 최댓값:
        최댓값 = x
        
print(최소값)