'''
1. def MENU():    << 메뉴 디자인 함수
2. def mnS():      << 메뉴선택 함수
3. def memIns():  << 회원가입 함수
4. def memSel():  << 회원 리스트 출력 함수
5. def memLog():  << 회원 로그인 함수
'''

def mnS():
	mnselect=input('\n\t메뉴의 번호를 선택해주세요.')
	if mnselect in menuChk:
		return int(mnselect)
	else:
		return 0

menu_select=input('메뉴를 선택해주세요: ')
mns(menu_select)
