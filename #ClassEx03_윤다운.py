class Customer:
    def __init__(self):
        self.cusBalance=0

    def deposit(self,num): #입금
        self.cusBalance+=num
        return self.cusBalance

    def withdraw(self,num): #출금
        self.cusBalance-=num
        return self.cusBalance

cus01=Customer()
cus02=Customer()

print(cus01.deposit(300))
print(cus01.withdraw(150))
print(cus02.deposit(400))
print(cus02.withdraw(150))

# function, class, module, package
# OS: 폴더명1\폴더명2\sample.py
# 객체: 폴더명1.폴더명2.sample.py

# self.cusBalance+=num
# self.cusBalance = self.cusBalance + num