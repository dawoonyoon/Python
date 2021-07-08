def add_many(*args):
    result=0
    cnt=0
    for i in args:
        print(args[cnt],end='\t')
        cnt=cnt+1
        result=result+1
    return result

result1=add_many(1,2)
print('=>합 {}'.format(result1))
print('-'*20)
result2=add_many(1,2,3)
print('=>합 {}'.format(result2))
