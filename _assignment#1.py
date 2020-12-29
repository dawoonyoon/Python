#Q1
answers=[]
numbers_given=[1,2,3,1]
for i in range(len(numbers_given)):
    for j in range(i+1,len(numbers_given)):
        if numbers_given[i]+numbers_given[j] not in answers:
            n=numbers_given[i]+numbers_given[j]
            answers.append(n)
answers.sort()
print(answers)

#Q2
number = int(input('숫자를 입력하세요: '))
n = 3
answer = ''
while number//3>=1:
    remain=number%3
    number=number//3
    answer=str(remain)+answer
    if number<3:
        answer=str(number)+answer
print(answer)

#Q3
numbers_given=[1,1,2,3,3,2]
for i in range(len(numbers_given)-2):
    for j in range(i+1,len(numbers_given)-1):
        if numbers_given[i]==numbers_given[j]:
            numbers_given.remove(numbers_given[j])
print(numbers_given)

#Q4
import random
computer=random.choice(['가위','바위','보'])
user=input('가위, 바위, 보 게임을 시작합니다. 셋 중 하나를 입력해주세요: ')
if (user=='가위' and computer=='보') or (user=='바위' and computer=='가위') or (user=='보' and computer=='바위'):
    print('사용자 승리')
elif (user=='보' and computer=='가위') or (user=='가위' and computer=='바위') or (user=='바위' and computer=='보'):
    print('사용자 패')
elif (user=='가위' and computer=='가위') or (user=='바위' and computer=='바위') or (user=='보' and computer=='보'):
    print('무승부')