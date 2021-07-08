a='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=html'
ya=a.split('?')
url = ya[0]
'''
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for i in range(len(list1)):
	print(list1[i], list2[i])

for i in list1:
	print(i)
'''
print(url)
print(ya[1])
print(ya[1].split('&'))
query_string = ya[1].split('&')
print(len(query_string))

for i in range(len(query_string)):
	print(query_string[i])

#for i in query_string:
#	print(i)
