#  최대값과 최소값을 뺀다.
# 나머지 값의 평균을 구한다.
def solution(scores):
    answer = 0
    return (sum(scores) - max(scores) - min(scores)) // (len(scores-2))

scores = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

print("solution 함수의 반환 값은 ", ret1, "ㅇ없습니다.") \


    # 체조 선수의