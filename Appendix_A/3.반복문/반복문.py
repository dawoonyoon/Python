# while문

# '1부터 9까지 각 정수의 합을 계산하는 코드'
i = 1
result = 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
print(result)

# 1부터 9까지의 수 중에서 홀수만 더하고자 할 때
i = 1
result = 0
# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)


# for문
"""
for 변수 in 리스트:
    실행할 소스코드
"""

result = 0
# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i
print(result)

scores = [90, 85, 77, 65, 97]
for i in range(5):
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

# 2번 학생과 4번 학생 블랙리스트
scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}
for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

# 2중 반복문 '구구단'
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()