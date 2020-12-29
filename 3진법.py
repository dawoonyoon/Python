number = int(input('숫자를 입력하세요: '))
answer = ''
while number//3>=1:
    remain=number%3
    number=number//3
    answer=str(remain)+answer
    if number<3:
        answer=str(number)+answer
print(answer)
answer = answer[::-1] #뒤집기
int_answer = int(answer)
new_list = []
print(int_answer)
for i in range(1, len(str(int_answer))+1):
    new_list.append(int_answer % (10**i) // 10**(i-1))
print(new_list)
sum = 0
power = 0
for i in new_list:
    test = i * (3**power)
    sum = sum + test
    power = power + 1
print(sum)
