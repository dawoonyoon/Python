def add_and_mul(a,b):
    return a+b
    return a*b  #return 두번 사용 -> 두번째 return 실행 x

result=add_and_mul(2,3)
print(result)
print('-'*10)

def say_nick(nick):
    if nick=='바보':
        return
    print('나의 별명은 {}입니다.' .format(nick))

say_nick('야호')
say_nick('바보')
print('-'*10)
