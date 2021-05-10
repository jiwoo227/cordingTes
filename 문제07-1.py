#펠런드롬 간단하게 만들어보기
#[0]과 [4]를 비교
#[1]과 [3]을 비교
########[2]는 비교 x

a = "neven"

if a[0] == a[4]:
    print("펠린드롬이 아니다.")
elif a[1] != a[3]:
    print("펠린드롬이 아니다.")
else:
    print("펠린드롬이다.")

#5글자인 경우
 #i값 0,i
for i in range(2):
    if a[i] != a[4-i]:
        print("펠린드롬이 아니다. ")


#7글자인경우
for i in range(3):
    if a[i] != a[6-i]:
        print("펠린드롬이 아니다. ")

else:
    print("펠린드롬이다.")

