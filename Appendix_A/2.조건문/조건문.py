x = 15

if x > 10:
    print(x)

"""
if 2.조건문 1:
    2.조건문 1이 True일 때 실행되는 코드
elif 2.조건문 2:
    2.조건문 1에 해당하지 않고, 2.조건문 2가 True일 때 실행되는 코드
else:
    위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드
"""

# 성적이 90점 이상일 때: A
# 성적이 90점 미만, 80점 이상일 때: B
# 성적이 80점 미만, 70점 이상일 때: C
# 성적이 70점 미만일 때: F

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')


score = 85
result = "Suceess" if score >= 80 else "Fail"
print(result)


a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)