ID= input("id를 입력해주세요:")
PWD= input("pwd를 입력해주세요:")
if ID == "Orange" and PWD == "1234":
	print("회원 인증 성공")
elif ID == "Orange" or PWD == "1234":
	print("아이디 또는 비밀번호 확인")
else:
	print ("회원 인증 실패")
