a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a)
print('-'*20)

a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)
