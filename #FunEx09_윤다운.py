def say_myself(name,old,man=True):
    print('나의 이름은 {}입니다.'.format(name))
    print('나이는 {}살 입니다.'.format(old))
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('박응용',27)
print('-'*20)
say_myself('박응선',27,False)
print('-'*20)
