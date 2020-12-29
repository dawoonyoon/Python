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

class SafeFourCal(FourCal):
    def div(self):
        if self.second==0: #나누는 값이 0인 경우 0을 리턴
            return 0
        
a=SafeFourCal(4,0)

print(a.first,'+',a.second,'=',a.sum())
print(a.first,'-',a.second,'=',a.sub())
print(a.first,'x',a.second,'=',a.mul())
print(a.first,'/',a.second,'=',a.div())