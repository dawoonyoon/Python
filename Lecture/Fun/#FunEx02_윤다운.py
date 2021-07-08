def add(a,b):
    return a,b,a+b
a,b,result=add(b=5,a=3)
print('{}+{}={}'.format(b,a,result))
print('-'*20)

def say():
    return 'Hi'
print(say())
print('-'*20)

def add2(a,b):
    print('{}, {}의 합은 {}입니다.'.format(a,b,a+b))
print(add2(3,4))
print('-'*20)

def say2():
    print('Hi')
say2()
print('-'*20)
