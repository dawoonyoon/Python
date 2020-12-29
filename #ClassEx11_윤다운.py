class Family():
    vI=10
    print(10)
    def __init__(self,first):
        self.vI01=first
        print("생성자:", self.vI01)

a=Family(10)
Family.vI+=10   #a.vI = 20
a.vI01+=10 #a.vI01 = 20

print(a.vI)
print(a.vI01)

b=Family(10)
Family.vI+=10    #b.vI = 30
b.vI01+=10  #b.vI01 = 20
print(b.vI)
print(b.vI01)

print(a.vI)
print(b.vI)

#print('--------')
print(id(a.vI))
print(id(b.vI))
print(id(Family.vI))

#print('--------')
Family.vI += 10
a.vI += 10
b.vI += 10
print(a.vI)
print(b.vI)
print(id(a.vI))
print(id(b.vI))
print(id(Family.vI))
Family.vI += 50
#print('--------')
print(a.vI)
print(b.vI)
print(Family.vI)