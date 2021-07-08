#immutable
#mutable

std = [1, 2, 3, 4,5]
std.append(14)
print(std)

animals = []
animals.append('코알라')
animals.append('하이에나') 
animals.append('바다소')
animals.append('땅다람쥐')
print(animals)
#.extend([]) 쌉가능
animals.extend(['목도리도마뱀','나무늘보'])
print(animals)

#humans라는 리스트를 만들지 않고 .append 때려박으면 안됨
humans = []
humans.append('윤다운')
print(humans)
#.append는 맨 뒤에 때려박기
#.insert는 맨 앞에 때려박기 _ insert(위치,때려박을 재료)
humans.insert(0,'박지성')
print(humans)
#.remove 첫 번째로 나오는 특정 재료 삭제
std.remove(1)
print(std)
#.pop 특정 재료가 아닌 위치를 지정해 재료를 삭제할 때
std.pop(0)
print(std)

animals.append('바다코끼리')
animals.append('아나콘다')
animals.append('스컹크')
print(animals)
animals.remove('나무늘보')
animals.remove('목도리도마뱀')
print(animals)
print(animals[3])
print(animals[4])
#animals.remove('바다코끼리')
del animals[4]
print(animals)
animals.append('바다코끼리')
print(animals)
print(animals[1:3])
#가나다 정렬
animals.sort()
print(animals)
animals.append('바다소')
print(animals)
del animals[1]
print(animals.count('바다소'))
print(len(animals))
 