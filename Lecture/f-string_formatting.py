#문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣습니다. 
s='coffee'
n=5
result1=f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result1)

#f-string 왼쪽 정렬
s1='left'
result2=f'|{s1:<10}|'
print(result2)
#f-string 가운데 정렬
s2='mid'
result3=f'|{s1:^10}|'
print(result3)
#f-string 오른쪽 정렬
s3='right'
result4=f'|{s1:>10}|'
print(result4)
