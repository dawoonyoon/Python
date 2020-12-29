
f1=open('새파일.txt','r')
line=f1.readline()
print(line)
f1.close()

# 모든 줄을 읽어서 화면에 출력하고 싶을때
f2=open('새파일.txt','r')
while True:
    line=f2.readline()
    if not line:break
    print(line)
f2.close()
