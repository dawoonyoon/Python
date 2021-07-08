class Family:
    lastname='김'

a=Family()
b=Family()

print(Family.lastname)
print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
