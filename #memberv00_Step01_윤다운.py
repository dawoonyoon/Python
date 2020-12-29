#MemberV00.py
menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []

print('='*16,'메뉴선택','='*16)
for m in range(len(menu)):
    print('%7s' % (menu[m]), end=' ')
print('')
print('='*41)
number = int(input('메뉴의 번호를 선택해주세요. '))
for i in range(len(menu)):
    if number == menu[m][0]:
        print(menu[m][1])
#print