cusBalance01=0
cusBalance02=0
def Customer01(chk,num):
    global cusBalance01

    if (chk==1):
        cusBalance01+=num
    elif (chk==2):
        cusBalance01-=num
    return cusBalance01

print(Customer01(1,300))
print(Customer01(2,150))

