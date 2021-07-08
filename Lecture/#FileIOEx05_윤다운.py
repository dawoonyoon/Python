with open('foo.txt','w') as f:
    f.write('Life is too short, you need python')

with open('foo.txt','r') as f2:
    data=f2.read()
    print(data)
