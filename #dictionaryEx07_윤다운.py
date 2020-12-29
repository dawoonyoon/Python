#dictionary 안에 찾으려는 key값이 없을 경우 미리 정해둔 default 값을
#대신 가져오게 하고 싶을 때에는 get(x,'default값')을 사용
#a dictionary에는 'foo'에 해당하는 값이 없다. 따라서 default 'bar' 돌려준다.
a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('foo','bar'))
print('-'*15)

# 해당 key가 dictionary 안에 있는지 확인하기(in)
a={'name':'pey','phone':'0119993323','birth':'1118'}
print('name' in a)
print('email'in a)