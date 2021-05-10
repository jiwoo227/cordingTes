def solution(price, grade):  # S 5프로, G 10프로, V 15프로
    reducedPrice = 0
    if grade == "S":
        return price - price*0.05
    if grade == "G":
        return price - price*0.10
    if grade == "V":
        return price - price*0.15


# testcase를 위한 output
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
