class Calculator:
    def __init__(self):
        self.result=0

    def adder(self,num):
        self.result+=num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class Fourcal:
    def setdata(self,first,second):
        self.first=first
        self.second=second

a=Fourcal()
a.setdata(4,2)

print(a.first)
print(a.second)
print(type(a))