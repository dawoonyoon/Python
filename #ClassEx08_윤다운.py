class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def sum(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class MoreFourCal(FourCal):
    pass
a=MoreFourCal(4,2)

print(a.first,'+',a.second,'=',a.sum())
print(a.first,'-',a.second,'=',a.sub())
print(a.first,'x',a.second,'=',a.mul())
print(a.first,'/',a.second,'=',a.div())