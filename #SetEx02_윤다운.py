s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

inter1=s1&s2
inter2=s1.intersection(s2)
print(inter1)
print(inter2)

print('-'*15)

vUnion1=s1|s2
vUnion2=s1.union(s2)
print(vUnion1)
print(vUnion2)

print('-'*15)

differ1=s1-s2
differ2=s2-s1

differ3=s1.difference(s2)
differ4=s2.difference(s1)

print(differ1)
print(differ2)
